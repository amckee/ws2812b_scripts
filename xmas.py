#!/usr/bin/env python3
# rpi_ws281x library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
"""
XMAS LED Strip Controller

A Python script for controlling WS2812B LED strips with Christmas-themed colors.
This script creates animated patterns using red, green, and white colors
to display festive lighting effects on LED strips connected to a Raspberry Pi.

Features:
- Color wipe animation with XMAS colors (red, green, white)
- Configurable LED strip parameters
- Graceful shutdown with optional LED clearing
"""

# Direct port of the Arduino NeoPixel library strandtest example.
# Showcases various animations on a strip of NeoPixels.

# Custom modded to use XMAS colors only

import time
import argparse
from rpi_ws281x import Adafruit_NeoPixel, Color

SLEEP_TIME = 0.25

# LED strip configuration:
LED_COUNT      = 150      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA,
                            LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).

def scroll(lights, light=0, wait_ms=50):
    """Wipe XMAS colors accross full light strip."""
    for i in range(lights.numPixels()):
        mod = (i + light) % 5
        if mod == 2:
            color = Color(255, 255, 255)
        elif mod == 0 or mod == 1:
            color = Color(0 , 255, 0)
        elif mod == 3 or mod == 4:
            color = Color(255, 0, 0)
        else:
            color = Color(0, 0, 255)

        lights.setPixelColor(i, color)
    lights.show()
    time.sleep(wait_ms/2000.0)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        mark = 0
        while True:
            if mark > 3:
                mark = 0
            #print ('Color wipe animations.')
            scroll(strip, mark) # Red/Green/White wipe
            time.sleep(SLEEP_TIME)
            mark += 1

    except KeyboardInterrupt:
        if args.clear:
            scroll(strip, Color(0,0,0), 10)
