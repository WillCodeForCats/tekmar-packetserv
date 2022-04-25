# Tekmar Packet Server (tekmar-packetserv)

Home Assistant Add-On for the Tekmar Gateway 482

https://github.com/WillCodeForCats/tekmar-packetserv

[![Open your Home Assistant instance and show the add add-on repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2FWillCodeForCats%2Ftekmar-packetserv)

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]
![Supports armhf Architecture][armhf-shield]
![Supports armv7 Architecture][armv7-shield]
![Supports i386 Architecture][i386-shield]

## Hardware

This Add-On requires additional hardware:

- Tekmar Gateway 482 (tN4 Gateway, RS232)
- RS232 serial port, such as a USB to Serial adapter.

## Installation

1. Navigate in your Home Assistant frontend to **Supervisor** -> **Add-on Store** and add this URL as an additional repository: `https://github.com/WillCodeForCats/tekmar-packetserv`
2. Find the "Tekmar Packet Server" add-on and click the "INSTALL" button.
3. Configure the add-on and click on "START".
4. Install the "Tekmar 482 Integration" from HACS or https://github.com/WillCodeForCats/tekmar-482

## Integration

This Add-On is used by the Tekmar 482 Integration. For more information,
refer to the the Integration documentation.

https://github.com/WillCodeForCats/tekmar-482

## Credits

Implemented using "tN4 Gateway 482 - Custom Integration Tools" and "Tekmar Home Automation
(tHA) Protocol" from: https://www.watts.com/products/hvac-hot-water-solutions/controls/control-accessories/482/482

Tekmar, tekmarNet, tN4, tN2, and related logos and trademarks are copyright 2021 Watts.

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
[armhf-shield]: https://img.shields.io/badge/armhf-yes-green.svg
[armv7-shield]: https://img.shields.io/badge/armv7-yes-green.svg
[i386-shield]: https://img.shields.io/badge/i386-yes-green.svg
