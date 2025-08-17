# Home Assistant Add-On: Tekmar Packet Server

The Tekmar Gateway 482 provides an RS232 serial interface to temkarNet thermostats, setpoint controls, and snow melting controls together with the [Tekmar Gateway 482 Integration](https://github.com/WillCodeForCats/tekmar-482) for Home Assistant.

## Hardware

This Add-On requires additional hardware:

- Tekmar Gateway 482 (tN4 Gateway, RS232)
- RS232 Serial Port or a USB to Serial adapter
- RS232 Serial to IP converter for Socket or RFC2217

## Integration

This Add-On is part of the Tekmar 482 Integration. Install this integration together with the add-on:

https://github.com/WillCodeForCats/tekmar-482

## Configuration

Install and connect the serial port as described in the Installation and Operation Manual
for the Tekmar Gateway 482. Connect the serial port on the Gateway 482 to the Home Assistant
serial port.

Select the serial device under "Configuration". This is required.

If you need to run the Tekmar Packet Server Add-On and Tekmar 482 Integration on different
systems, enter a port number to remotely access this Add-On. This is useful if your Tekmar
Gateway 482 is in a different location, such as a boiler room. The Integration will
communicate with the Add-On across your LAN.

### Serial Port Configuration

Serial Port Mode: device

- For a locally connected USB to serial adapter

Serial Port Mode: socket

- For a IP to serial port server using a TCP socket connection.

Serial Port Mode: rfc2217

- For a IP to serial port server using a TCP connection using the RFC2217 protocol.

For "socket" and "rfc2217" types you will also need to configure the parameters for Serial Server IP and Serial Server Port.

On IP-to-Serial servers use "9600,8,N,1" for the serial port:

- Baud Rate 9600
- Eight Bits
- No Parity
- One Stop Bit

## Known Issues and Limitations

- If serial communications are lost the packet server won't show an error until the next
  new incoming connection.
- Any errors will cause the packet server to stop, and it will need to be
  restarted manually or by enabling the "watchdog" option.

## Credits

Implemented using "tN4 Gateway 482 - Custom Integration Tools" and "Tekmar Home Automation
(tHA) Protocol" from: https://www.watts.com/products/hvac-hot-water-solutions/controls/control-accessories/482/482

Tekmar, tekmarNet, tN4, tN2, and related logos and trademarks are copyright 2021 Watts.
