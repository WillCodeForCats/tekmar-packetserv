# Tekmar Packet Server (tekmar-packetserv)
![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]
![Supports armhf Architecture][armhf-shield]
![Supports armv7 Architecture][armv7-shield]
![Supports i386 Architecture][i386-shield]

This is a Home Assistant Add-On used by the [Tekmar Gateway 482 Integration](https://github.com/WillCodeForCats/tekmar-482) to communicate with your Tekmar networked thermostats, setpoint controls, and snow melting controls.

## Hardware

This Add-On requires additional hardware:

- Tekmar Gateway 482 (tN4 Gateway, RS232)
- RS232 Serial Port or a USB to Serial adapter
- RS232 Serial to IP converter for Socket or RFC2217

## Installation

[WillCodeForCats/tekmar-packetserv/wiki/Installation](https://github.com/WillCodeForCats/tekmar-packetserv/wiki/Installation)

[![Open your Home Assistant instance and show the add add-on repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FWillCodeForCats%2Ftekmar-packetserv)

Add-On Store Repository Address: `https://github.com/WillCodeForCats/tekmar-packetserv`

## Integration

This Add-On is part of the Tekmar 482 Integration. Install this integration together with the add-on:

[WillCodeForCats/tekmar-482](https://github.com/WillCodeForCats/tekmar-482)

## Credits

Implemented using "tN4 Gateway 482 - Custom Integration Tools" and "Tekmar Home Automation
(tHA) Protocol" from: https://www.watts.com/products/hvac-hot-water-solutions/controls/control-accessories/482/482

Tekmar, tekmarNet, tN4, tN2, and related logos and trademarks are copyright 2021 Watts.

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
