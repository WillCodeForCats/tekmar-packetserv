#!/usr/bin/with-contenv bashio
export SERIAL_DEV=$(bashio::config 'serial_device')
export IP4_ACL=$(bashio::config 'ip_access_permit')

python3 /server/packetserv.py
