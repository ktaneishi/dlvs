#!/bin/sh

COMMUNITY=public
IPADDRESS=xxx.xxx.xxx.xxx

snmpwalk -v 2c -c $COMMUNITY $IPADDRESS iso.3.6.1.4.1.21317.1.3.2.2.3.4.8.2.1.0
snmpwalk -v 2c -c $COMMUNITY $IPADDRESS iso.3.6.1.4.1.21317.1.3.2.2.3.4.8.2.2.0
for i in $(seq 1 8)
do snmpwalk -v 2c -c $COMMUNITY $IPADDRESS iso.3.6.1.4.1.21317.1.3.2.2.2.2.1.1.2.$i
done