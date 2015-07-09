#!/bin/sh

cd $DREAMSERVER_HOME

# If the server is already running, terminate.
if [ -f server.pid ]; then
	if ps x | grep main.py | grep `cat server.pid` | grep -q -v grep >/dev/null; then
		exit
	fi
fi

# Otherwise, start the server.
./main.py >/dev/null 2>&1 &
echo $! > server.pid
