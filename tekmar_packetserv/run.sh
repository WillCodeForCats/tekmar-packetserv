#!/usr/bin/with-contenv bashio
SERIAL_DEVICE=$(bashio::config 'device')
IP4_ACL=$(bashio::config 'ip4_acl')

python3 server/packetserv.py ${SERIAL_DEVICE}
