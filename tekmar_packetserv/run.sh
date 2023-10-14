#!/usr/bin/with-contenv bashio
export SERIAL_MODE=$(bashio::config 'serial_mode')
export SERIAL_DEV=$(bashio::config 'serial_device')
export SERIAL_SRV_HOST=$(bashio::config 'serial_server_host')
export SERIAL_SRV_PORT=$(bashio::config 'serial_server_port')
export IP4_ACL=$(bashio::config 'ip_access_permit')

python3 /server/packetserv.py
