"""Allow reading and writing of packets using the tpck protocol.

The tpck protocol provides data delimiting and validation for
communication links that can not support the simplicity of the
string-based packet transfer.
"""

# ******************************************************************************
import packet

# ******************************************************************************
_SOF_CODE = 0xCA  # Start-of-frame
_EOF_CODE = 0x35  # End-of-frame
_ESC_CODE = 0x2F  # Escape (stuffing)


# ******************************************************************************
_stuff_list = (_SOF_CODE, _EOF_CODE, _ESC_CODE)


# ******************************************************************************
def serialize(p):
    """Take a packet object and convert it to a string of bytes that conform
    to the tpck protocol.

    Return the resulting sequence which will include start and end of
    frame delimiters along with escape characters and a checksum to
    validate the data.
    """

    def stuff_byte(b):
        if b in _stuff_list:
            build.append(_ESC_CODE)
        build.append(b)

    build = [_SOF_CODE]
    stuff_byte(len(p.data))
    stuff_byte(p.type)
    for i in p.data:
        stuff_byte(i)
    stuff_byte(_calc_checksum(p.type, p.data))
    build.append(_EOF_CODE)
    return build


# ******************************************************************************
def parse(bytes, state=None):
    """From a stream of bytes, parse out packets using the tpck protocol.

    A state object is used to keep track of the state of packets that
    span calls to this function, i.e. if a packet is split over more than
    one sequence of bytes, the state object will keep track of it.

    Return a list of all packets that can be parsed from the sequence
    of bytes.

    Usage is simple:
        state_obj = None
        while True:
            bytes = stream_obj.read()
            packet_list = tpck.parse(bytes, state_obj)
            for p in packet_list:
                print p
    """
    packets = []
    if state is None:
        state = _TpckRxState()
    try:
        while True:
            if state.feed(bytes.pop(0)):
                packets.append(packet.Packet(state.type, state.data))
                state.reset()
    except IndexError:
        return packets, state


# ******************************************************************************
def _calc_checksum(type, data):
    return sum(data, type + len(data)) & 0xFF


# ******************************************************************************
class _TpckRxState:
    """Receiver state object implemented by generator functions (similar to
    protothreads.
    """

    # --------------------------------------------------------------------------
    def __init__(self):
        self.reset()

    # --------------------------------------------------------------------------
    def reset(self):
        self.type = 0
        self.data = []
        self.cs = 0
        self.i = self.rx_packet()
        self.underway = True

    # --------------------------------------------------------------------------
    def rx_byte(self):
        """Receive a byte and skip escape characters."""
        if self.byte == _ESC_CODE:
            yield

    # --------------------------------------------------------------------------
    def rx_packet(self):
        """Generator (protothread) to receive a packet."""
        # Wait for start of frame.
        while self.byte != _SOF_CODE:
            yield
        yield

        # Read the length of the data.
        for temp in self.rx_byte():
            yield
        self.data = [0] * self.byte
        yield

        # Read the type of the packet.
        for temp in self.rx_byte():
            yield
        self.type = self.byte
        yield

        # Read each data byte.
        for i in range(len(self.data)):
            for temp in self.rx_byte():
                yield
            self.data[i] = self.byte
            yield "Data" + str(i) + "=" + str(self.byte)

        # Read the checksum.
        for temp in self.rx_byte():
            yield
        self.cs = self.byte
        yield

        # Read bytes until an end-of-frame is received.
        while self.byte != _EOF_CODE:
            yield

    # --------------------------------------------------------------------------
    def feed(self, b):
        """Accept bytes from a stream and feed them through the generator
        functions.  This acts as a 'supervisor' to the generator 'mini-
        threads' to handle the case where an un-escaped start-of-frame
        character is recieved while receiving another packet.
        """
        self.byte = b
        if b == _SOF_CODE and not self.underway:
            self.reset()
            next(self.i)
        else:
            try:
                next(self.i)
            except StopIteration:
                self.underway = False
                if _calc_checksum(self.type, self.data) == self.cs:
                    return True
        return False
