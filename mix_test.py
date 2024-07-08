from time import sleep
import RPi.GPIO as GPIO
from utils import *
from rpi_ws281x import *
from stripp import strip


#strip ledss
empty = Color(0,0,0)
blue = Color(0,0,255)
green = Color(0, 255, 0)
red = Color(255, 0, 0)
orange = Color(102, 51, 0)
yellow = Color(255, 255, 0)
white = Color(255, 255, 255)
strip_leds =  strip()
strip_leds.clear_all()



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
                        print(blue)
                        strip_leds.set_color_all(Color(0,0,255))
                        while  True:
                            if detectObject_proximity(blue_proximity_pin):
                            #turn_led_on(blue_pin)

                                turn_led_off(blue_pin)
                                turn_led_on(green_pin)
                                strip_leds.set_color_all(green)
                                break
                    elif trash_class == "yellow":
                        
                        turn_led_on(yellow_pin)
                        strip_leds.set_color_all(yellow)
                        while True:
                            if detectObject_proximity(yellow_proximity_pin):
                                turn_led_off(yellow_pin)
                                turn_led_on(green_pin)
                                strip_leds.set_color_all(green)
                                break
                              
                    else: #brown
                        turn_led_on(brown_pin)
                        strip_leds.set_color_all(orange)
                        while True:
                            if detectObject_proximity(brown_proximity_pin):
                                turn_led_off(brown_pin)
                                turn_led_on(green_pin)
                                strip_leds.set_color_all(green)
                                break


                    
                                
                    
                    object_detected = False
                    sleep(2)
                    turn_led_off(green_pin)
                    strip_leds.clear_all()
    else: 
        if  detectObject_proximity(detect_object_sensor):
            object_detected = True
            print("something detected")
            acc = 30 


    
            
            
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        break
    



    
    #GPIO.cleanup()






