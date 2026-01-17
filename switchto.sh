#!/bin/bash

basepath="$HOME/bin/ws2812b_scripts/"

if [ -z "$1" ]; then
	echo "nothing given"
	exit 1
elif [ ! -f "$basepath/$1.py" ]; then
	echo "file not found"
	exit 2
fi

sudo pkill python
sleep .5
sudo $basepath/$1.py &

exit 0
