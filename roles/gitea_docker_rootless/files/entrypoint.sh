#!/bin/sh

if [ -z "${USER_UID}" ] || [ -z "${USER_GID}" ]; then
  echo "Please set USER_UID and USER_GID"
  exit 1
fi

echo "Syncer launched."

# Initial sync and ownership change
cp /source/* /destination
chown -R "${USER_UID}:${USER_GID}" /destination

echo "Copied initial files"

counter=0
# Watch for changes and sync periodically
inotifywait -m -e modify /destination |
while read FILE; do
  counter=$((counter + 1))
  echo "Registered change ${counter}: $FILE"
  cp /destination/authorized_keys /source
  chown 0:0 /source/authorized_keys
done

echo "Exited loop"
