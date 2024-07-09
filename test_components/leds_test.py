import RPi.GPIO as GPIO
import time
from test_components.proximity_test import initialInductive, detectObject

blue_pin = 4
yellow_pin = 14
brown_pin = 17
green_pin = 22
blue_proximity_pin = 19
white_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def turn_led(led_pin): 
    GPIO.setup(led_pin ,GPIO.OUT)
    print("LED on")
    GPIO.output(led_pin,GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(led_pin,GPIO.LOW)


async def waiting(led_pin):
    GPIO.setup(led_pin ,GPIO.OUT)
    print("LED on")
    GPIO.output(led_pin,GPIO.HIGH)
    await time.sleep(0.5)
    print("LED off")
    GPIO.output(led_pin,GPIO.LOW)
    await time.sleep(0.5)



turn_led(blue_pin)
turn_led(yellow_pin)
turn_led(brown_pin)
turn_led(white_pin)
turn_led(green_pin)




#initialInductive(blue_proximity_pin)
check = True
while True:
    
    #while not detectObject() and check:
    waiting(white_pin)
    waiting(brown_pin)
        
        
    #else:
        #check = False
        #turn_led(blue_pin)
        #turn_led(green_pin)
    


