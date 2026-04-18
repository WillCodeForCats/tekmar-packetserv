# Tekmar Packet Server (tekmar-packetserv)

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]

This is a Home Assistant App used by the [Tekmar Gateway 482 Integration](https://github.com/WillCodeForCats/tekmar-482) to communicate with your Tekmar networked thermostats, setpoint controls, and snow melting controls.

## Hardware

This App requires additional hardware:

- Tekmar Gateway 482 (tN4 Gateway, RS232)
- RS232 Serial Port or a USB to Serial adapter
- RS232 Serial to IP converter for Socket or RFC2217

Important: This App can only be used with the Gateway 482. The touchscreen Gateway 486 IS NOT compatible because it doesn't have a local API.

## Installation

[WillCodeForCats/tekmar-packetserv/wiki/Installation](https://github.com/WillCodeForCats/tekmar-packetserv/wiki/Installation)

[![Open your Home Assistant instance and show the add app repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FWillCodeForCats%2Ftekmar-packetserv)

App Store Repository Address: `https://github.com/WillCodeForCats/tekmar-packetserv`

## Integration

This App is part of the Tekmar 482 Integration. Install this integration together with the App:

[WillCodeForCats/tekmar-482](https://github.com/WillCodeForCats/tekmar-482)

## Credits

Implemented using "tN4 Gateway 482 - Custom Integration Tools" and "Tekmar Home Automation
(tHA) Protocol" from: [https://www.watts.com/products/hvac-hot-water-solutions/controls/control-accessories/482/482](https://www.watts.com/products/hvac-hot-water-solutions/controls/control-accessories/482/482)

Tekmar, tekmarNet, tN4, tN2, and related logos and trademarks are copyright 2021 Watts.

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg