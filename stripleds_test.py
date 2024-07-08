import time
import math
import random
from rpi_ws281x import *

from utils import *


LED_COUNT      = 60         # Number of LED pixels.
LED_PIN        = 18         # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000     # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10         # DMA channel to use for generating a signal (try 10)
LED_BRIGHTNESS = 65         # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False      # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0          # set to '1' for GPIOs 13, 19, 41, 45 or 53


strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()
strip.setPixelColor(15, Color(0,255,255))
strip.show()
'''
def set_color_all(color):
    for i in range(LED_COUNT):
        strip.setPixelColor(i, color)
    strip.show()

def clear_all():
    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(0,0,0))
    strip.show()

def waiting(color):
    set_color_all(color)
    time.sleep(1)
    set_color_all(empty)
    time.sleep(1)
    
'''

empty = Color(0,0,0)
blue = Color(0,0,255)
green = Color(0, 255, 0)
red = Color(255, 0, 0)
yellow = Color(255, 255, 0)
white = Color(255, 255, 255)
colors = [blue, green, red, yellow, white]
for color in colors:

    set_color_all(color)
    time.sleep(1.5)



waiting(white)
clear_all()












