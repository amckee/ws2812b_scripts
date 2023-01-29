#!/usr/bin/env python3
# rpi_ws281x library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

# Custom modded to use XMAS colors only

import time
from rpi_ws281x import *
import argparse
 
# LED strip configuration:
LED_COUNT      = 150      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
 
def colorWipe(strip, mark=0, wait_ms=50):
    """Wipe XMAS colors accross full strip."""
    for i in range(strip.numPixels()):
        mod = (i + mark) % 5
        if mod == 2:
            color = Color(255, 255, 255)
        elif mod == 0 or mod == 1:
            color = Color(0 , 255, 0)
        elif mod == 3 or mod == 4:
            color = Color(255, 0, 0)

        strip.setPixelColor(i, color) 
    strip.show()
    time.sleep(wait_ms/2000.0)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
 
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
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
            colorWipe(strip, mark) # Red/Green/White wipe
            time.sleep(50/2000)
            mark += 1
 
    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
