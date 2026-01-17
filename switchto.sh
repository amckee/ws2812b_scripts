#!/bin/bash

basepath="$HOME/bin/ws2812b_scripts/"

if [ -z "$1" ]; then
	echo "nothing given"
	exit 1
fi

if [ -f "$basepath/$1.py" ]; then
	sudo pkill python
	sleep .5
	sudo $basepath/$1.py &
fi

exit 0
