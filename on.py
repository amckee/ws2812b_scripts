#!/usr/bin/python2

# Uses RED by default to signal an error with a few styles:
# spin (works best with circular lights)
# blink
# blink with fade in/out

import time, argparse
from neopixel import *

# LED strip configuration:
LED_COUNT       = 150      # Number of LED pixels.
LED_PIN         = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ     = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA         = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS  = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT      = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL     = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
ON 	        = Color(255, 255, 255)
OFF             = False #Color(0, 0, 0) #using False works the same
sleeptime       = .5 # set a default delay

def all(strip, color=OFF):
    #quick function to set all lights at once
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
    
if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    all( strip, ON )
