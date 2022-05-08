#!/usr/bin/env python3

""" Packet server application.
    """


#******************************************************************************
import sys
import os
import datetime
import serial
import threading
import socket
import struct
import tpck
import select
import packet
import ipaddress
import traceback


#******************************************************************************
# Timeout used for serial port and socket reads.
TIMEOUT = 0.1

# Number of bytes from the serial port to process at any given time.
READ_SIZE = 100


#******************************************************************************
def message(msg):
    """ Emit a time-stamped message.
        """
    msg_str = "{}: {}"
    print(msg_str.format(str(datetime.datetime.now()), msg), flush=True)


#******************************************************************************
def shut_down(msg, ser_thrd, connections):
    """ Shut down the server, closing all socket connections and the serial
        port.
        """
    message(msg)
    connections.lock.acquire()
    for c in connections.lst:
        close_socket(c)
    connections.lst = []
    connections.lock.release()
    ser_thrd.stop()


#******************************************************************************
def close_socket(s):
    """ Shut down a connection to a socket.  This accepts a Connection
        instance, not a socket.
        """
    message('Closing connection to %s:%d' % (s.addr[0], s.addr[1]))
    try:
        s.sock.shutdown(2)
    except socket.error:
        pass
    s.sock.close()

#******************************************************************************
def check_thread_alive(thr):
    thr.join(timeout=0.0)
    return thr.is_alive()

#******************************************************************************
class Connection:
    """ Container for a socket and its address.

        We use this to maintain the
        address of a socket even after it has died.
        """

    #--------------------------------------------------------------------------
    def __init__(self, sock, addr):
        """ An connection is created with a socket and an address-tuple.
            """
        self.sock = sock
        self.addr = addr


#******************************************************************************
class ConnectionList:
    """ Thread-safe list of Connection objects.
        """

    #--------------------------------------------------------------------------
    def __init__(self):
        self.lock = threading.RLock()
        self.lst = []


    #--------------------------------------------------------------------------
    def find_socket(self, sock):
        """ Find a socket in the list and return the containing Connection
            object.

            Return None if it isn't found.
            """
        for s in self.lst:
            if s.sock == sock:
                return s
        return None


#******************************************************************************
class RunSerial(threading.Thread):

    #--------------------------------------------------------------------------
    def __init__(self, port, connect_list):
        """ Pass in the serial port and a reference to a list of connections.
            """
        threading.Thread.__init__(self, name = 'Serial Port Listener')
        self.port = port
        self.connections = connect_list
        self.running = False


    #--------------------------------------------------------------------------
    def get_fmt(len_obj):
        """ Return a format string (as required by struct methods) that can
            be used to pack a list of or unpack a string of bytes.

            The length of the returned format string will be the length of the
            len_obj argument.
            """
        return ''.join(['B'] * len(len_obj))

    get_fmt = staticmethod(get_fmt)


    #--------------------------------------------------------------------------
    def run(self):
        """ Watch the serial port.

            Send any received packets to all connected sockets.
            
            If any data is received from any of the connected sockets, convert
            that data to packets and send it to the serial port.

            If any sockets die, remove them from the connection list.
            """
        self.running = True
        tpck_state = None
        try:
            while self.running:
                # Read packets and store them in string form in send_data
                byte_str = self.port.read(READ_SIZE)
                fmt = RunSerial.get_fmt(byte_str)
                bytes = list(struct.unpack(fmt, byte_str))
                pck_list, tpck_state = tpck.parse(bytes, tpck_state)
                send_data = ''.join([str(p) for p in pck_list])

                # Make a list of socket objects from the connection list.
                self.connections.lock.acquire()
                sock_list = [c.sock for c in self.connections.lst]
                self.connections.lock.release()

                # Removals is a list of dead or dying sockets.
                removals = []
                rl, wl, _ = select.select(sock_list, sock_list, [], TIMEOUT)

                for r in rl:
                    try:
                        rx_str = r.recv(1024)

                        # Read data, pack it, then send it.
                        for s in [s for s in rx_str.rsplit('\n'.encode()) if s]:
                            pck_bytes = tpck.serialize(packet.Packet.from_str(s))
                            fmt = RunSerial.get_fmt(pck_bytes)
                            self.port.write(struct.pack(fmt, *pck_bytes))

                    except socket.error:
                        # rx_str == '' should indicate that a socket closed.  It seems that
                        # this method is required for the cygwin platform as the closed socket
                        # shows up in the readable list, but can't be read from.
                        removals.append(r)

                for w in wl:
                    # Write received data to connected sockets that are still
                    # alive.
                    if w not in removals:
                        try:
                            w.send(send_data.encode())

                        except socket.error:
                            removals.append(w)

                # Remove dead and dying sockets from the connection list.
                self.connections.lock.acquire()
                for r in removals:
                    s = self.connections.find_socket(r)
                    if s is not None:
                        close_socket(s)
                        self.connections.lst.remove(s)
                self.connections.lock.release()

        except serial.SerialException as err:
            self.running = False
            message(err)
            
        except:
            # Expected exception handling is buried in the calls within this
            # thread.  Anything else is to major to handle and is most likely
            # caused by the main server thread being killed.
            self.running = False
            message(traceback.format_exc())
        
        # Shut down the thread.  Wrap the port-close in a try block in case
        # we are here because the port got closed.
        message('Serial port closing.')
        try:
            self.port.close()
        except (select.error, serial.SerialException):
            pass


    #--------------------------------------------------------------------------
    def stop(self):
        """ Shut down the serial port thread and wait for it to end.
            """
        message('Stopping serial thread.')
        self.running = False
        self.join()


#******************************************************************************
if __name__ == '__main__':
    try:
        ser_name = os.environ.get('SERIAL_DEV')
        env_ipv4_acl = os.environ.get('IP4_ACL')
        host_addr = '0.0.0.0'
        port_id = 3000
        ip4_acl = ipaddress.IPv4Network(env_ipv4_acl)

    except ValueError:
        print(f"address/netmask is invalid: {env_ipv4_acl}")

    else:
        message(f"Starting Tekmar Packet Server...")
        message(f"Process ID = {os.getpid()}")

        message(f"Opening serial port: {ser_name}")
        try:
            serial_port = serial.Serial(ser_name, timeout = TIMEOUT)

        except serial.SerialException:
            message('Could not open serial port. Exiting.')

        else:
            connections = ConnectionList()
            serial_thread = RunSerial(serial_port, connections)
            serial_thread.start()
            message('Starting serial thread.')

            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.bind((host_addr, port_id))
                sock.listen(1)
                message(f"IPv4 Access List: {ip4_acl}")
                message('Waiting for incoming connections.')

            except socket.error:
                message('Could not open socket at %s:%d' % (host_addr, port_id))
                serial_thread.stop()

            else:
                try:
                    while True:
                        c, a = sock.accept()

                        if ipaddress.IPv4Address(a[0]) in ip4_acl:
                            connections.lock.acquire()
                            connections.lst.append(Connection(c, a))
                            connections.lock.release()
                            if not check_thread_alive(serial_thread):
                                raise ConnectionError('Serial port thread is not running!')
                            message('Connected to %s:%d' % (a[0], a[1]))

                        else:
                            c.close()
                            message(f"Connection refused: {a[0]} not in {env_ipv4_acl}")

                except socket.error as err:
                    message(err)
                    shut_down('Socket error. Forcing shutdown.', serial_thread, connections)
                    
                except ConnectionError as err:
                    message(err)
                    shut_down('Exception. Forcing shutdown.', serial_thread, connections)
                
                except:
                    message(traceback.format_exc())
