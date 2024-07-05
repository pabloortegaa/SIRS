from time import sleep
import RPi.GPIO as GPIO
from utils import *

#Proximity sensors pins
detect_object_sensor_pin = 26
blue_proximity_pin = 19
yellow_proximity_pin = 12
brown_proximity_pin = 13

#LEDS pins
blue_pin = 27
yellow_pin = 14
brown_pin = 17
green_pin = 22
blue_proximity_pin = 19
white_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


detect_object_sensor = initialInductive(detect_object_sensor_pin)
blue_proximity = initialInductive(blue_proximity_pin)
yellow_proximity = initialInductive(yellow_proximity_pin)
brown_proximity = initialInductive(brown_proximity_pin)




object_detected = False


# Start screening with the camera
cap = cv2.VideoCapture(0)
acc = 0

while True:
    ret, frame = cap.read()
    #acc +=1
    
    
    #cv2.imshow('frame', frame)
    
        

    if object_detected:
        print("aqui2")
        if acc > 1:
            acc-=1
        if acc == 1:
            acc = 0
            trash_class = apply_yolo(frame)            
            if trash_class != "":
                    if trash_class == "blue":
                        turn_led_on(blue_pin)
                        while  True:
                            if detectObject_proximity(blue_proximity_pin):
                            #turn_led_on(blue_pin)
                            
                                turn_led_off(blue_pin)
                                turn_led_on(green_pin)
                                break
                    elif trash_class == "yellow":
                        
                        #turn_led_on(yellow_pin)
                        while not detectObject_proximity(yellow_proximity_pin):
                            turn_led_on(yellow_pin)
                        turn_led_on(green_pin)
                              
                    else: #brown
                        #turn_led_on(brown_pin)
                        while not detectObject_proximity(brown_proximity_pin):
                            turn_led_on(brown_pin)
                        turn_led_on(green_pin)


                    
                                        #turn_led_on(white_pin)
                    
                    object_detected = False
    else: 
        if  detectObject_proximity(detect_object_sensor):
            object_detected = True
            print("something detected")
            acc = 30 


    
            
            
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        break
    



    
    #GPIO.cleanup()






