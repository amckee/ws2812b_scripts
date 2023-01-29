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

def spin( strip, loops=1 ):
    """Spin red around the LEDs"""
    print("Spinning %s times" % loops)
    sleeptime = .1
    sleeptime = sleeptime / strip.numPixels()
    stop = False
    
    while not stop:
    #for loopcnt in range( loops ):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, RED)
            strip.show()
            time.sleep(sleeptime)
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, OFF)
            strip.show()
            time.sleep(sleeptime)

def spin_gap( strip, loops=1, gap=3 ):
    """Like spin() but leaves a gap between lit segments"""
    if loops > 0:
      print("Spinning with gap %s times" % loops)
    elif loops == -1:
      print("Spinning lights indefinitely")
    else:
      print("how did you get here?")

    sleeptime = .5
    sleeptime = sleeptime / strip.numPixels()
    offset = 1 # offset for shifting around
    count = 3 # width of the on-off gap
    stop = False
    loopcount = 0

    while not stop:
    #for loopcnt in range( loops ):
        loopcount += 1 #track loops
        ## make the gaps
        lightson = True
        for i in range( strip.numPixels() ):
            if i%count == 0:
                lightson = not lightson

            if lightson:
                strip.setPixelColor(i+offset, RED)
            else:
                strip.setPixelColor(i+offset, OFF)
            strip.show()
        strip.show()
        print("offset:%s" % offset)
        time.sleep( sleeptime )
        offset += 1 # setup next round for spin effect
        if loops > 0 and loopcount > loops:
          stop = True
	if offset > strip.numPixels():
          offset = 1

if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
    setall(strip, OFF)
    strip.show()

    print("numPixels:%s" % strip.numPixels())
    
    #spin( strip, loops=2 )
    #blink( strip, loops=2 )
    #blink_fade( strip, loops=2 )
    spin( strip, loops=-1 )

    print("Shutting them all off")
    setall(strip, OFF)
