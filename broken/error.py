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
RED             = Color(0, 255, 0)
OFF             = False #Color(0, 0, 0) #using False works the same
sleeptime       = .5 # set a default delay

def setall( strip, color=OFF ):
    #quick function to set all lights at once
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

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

def blink_fade( strip, loops=1 ):
    """Like blink() but fade in and out"""
    print("Blink fading %s times" % loops)
    sleeptime = .025 # speed it up for a nice fade rate
    brightness = 0 # track brightness level
    step = 10 # how much do we change the brightness on each step
    color = Color(0, brightness, 0) # set initial color
    
    # calculate max brightness with given step
    maxbright = 254 - step

    setall( strip, OFF )

    for loopcnt in range( loops ):
        brightness = 0 + step
        while brightness > 0: # run until lights are off again
            # set the currently decided on color
            setall( strip, Color(0, brightness, 0) )
            #strip.setBrightness( brightness ) ##does nothing

            ## setup next color
            # if we are fading in and if we are at max brightness...
            if step > 0 and brightness > maxbright:
                step = step * -1 # we are now fading out

            brightness += step
            strip.show()
            time.sleep( sleeptime )
        step = step * -1 # should always reset back to a positive number
    
def spin( strip, loops=1 ):
    """Spin red around the LEDs"""
    print("Spinning %s times" % loops)
    sleeptime = .1
    sleeptime = sleeptime / strip.numPixels()
    
    for loopcnt in range( loops ):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, RED)
            strip.show()
            time.sleep(sleeptime)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, OFF)
            strip.show()
            time.sleep(sleeptime)

def spin_gap( strip, loops=1, gap=5 ):
    """Like spin() but leaves a gap between lit segments"""
    print("Spinning with gap %s times" % loops)
    sleeptime = .5
    sleeptime = sleeptime / strip.numPixels()
    offset = 1 # offset for shifting around
    count = 5 # width of the on-off gap

    for loopcnt in range( loops ):
        ## make the gaps
        lightson = True
        for i in range( strip.numPixels() ):
            print("offset:%s" % offset)
            if i%count == 0:
                lightson = not lightson

            #i += offset
            if i+offset > strip.numPixels():
                offset = 1

            if lightson:
                strip.setPixelColor(i+offset, RED)
            else:
                strip.setPixelColor(i+offset, OFF)
            strip.show()
        strip.show()
        time.sleep( sleeptime )
        offset += 1 # setup next round for spin effect

if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    setall(strip, OFF)
    strip.show()

    print("numPixels:%s" % strip.numPixels())
    
    #spin( strip, loops=2 )
    #blink( strip, loops=2 )
    #blink_fade( strip, loops=2 )
    spin_gap( strip, loops=10 )

    print("Shutting them all off")
    setall(strip, OFF)
