#!/usr/bin/python2

# Uses RED by default to signal an error with a few styles:
# spin (works best with circular lights)
# blink
# blink with fade in/out

import time
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT       = 150      # Number of LED pixels.
LED_PIN         = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ     = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA         = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS  = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT      = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL     = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
RED             = Color(0, 255, 0)
OFF             = False #Color(0, 0, 0) #using False works the same
sleeptime       = .5 # set a default delay

def all(strip, color=OFF):
    #quick function to set all lights at once
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
    
def spin( strip, loops=1 ):
    """Spin red around the LEDs"""
    print("Spinning %s times" % loops)
    sleeptime = .1
    sleeptime = sleeptime / LED_COUNT
    
    for loopcnt in range( loops ):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, RED)
            strip.show()
            time.sleep(sleeptime)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, OFF)
            strip.show()
            time.sleep(sleeptime)

def blink( strip, loops=1 ):
    """Blink the strip on and off"""
    print("Blinking %s times" % loops)
    fadein = True # track if fading in or out

    for loopcnt in range( loops ):
        if fadein:
            for i in range( strip.numPixels() ):
                strip.setPixelColor(i, RED)
        else:
            for i in range( strip.numPixels() ):
                strip.setPixelColor(i, OFF)
        fadein = not fadein
        strip.show()
        time.sleep( sleeptime )

def blinkfade(strip, loops=0):
    """Like blink() but fade in and out"""
    print("Blink fading %s times" % loops)
    sleeptime = .025 # speed it up for a nice fade rate
    #fadein = True # track if fading in or out  #using step = -1 instead
    brightness = 0 # track brightness level
    step = 10 # how much do we change the brightness on each step
    color = Color(0, brightness, 0) # set initial color
    
    # calculate max brightness with given step
    maxbright = 254 - step

    all( strip, OFF )

    for loopcnt in range( loops ):
        brightness = 0 + step
        while brightness > 0: # run until lights are off again
            # set the currently decided on color
            all( strip, Color(0, brightness, 0) )

            ## setup next color
            # if we are fading in and if we are at max brightness...
            if step > 0 and brightness > maxbright:
                step = step * -1 # we are now fading out

            brightness += step
            strip.show()
            time.sleep( sleeptime )
        step = step * -1 # should always reset back to a positive number
    
if __name__ == '__main__':
    # Process arguments
    #parser = argparse.ArgumentParser()
    #parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    #args = parser.parse_args()

    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    all(strip, OFF) #start with all lights off
    strip.show()
    
    #spin( strip, 2 )
    #blink( strip, 5 )
    blinkfade( strip, 3 )
    spin( strip, 3 )
    blinkfade( strip, 3 )

    print("Shutting them all off")
    all(strip, OFF)
