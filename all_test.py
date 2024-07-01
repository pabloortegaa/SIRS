import cv2
from ultralytics import YOLO
from gpiozero import Servo, DistanceSensor
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

import RPi.GPIO as GPIO




# activate motors
factory = PiGPIOFactory()
servo_1 = Servo(12, pin_factory=factory)
servo_2 = Servo(2, pin_factory=factory)

servo_1.min()
servo_2.min()

def move_servo(servoo):

    print("moving to min pos")
    servoo.min()
    sleep(1)
    
    print("moving to mid position")
    servoo.max()
    sleep(3)

    #print("moving to max pos")
    #servoo.max()
    #sleep(1)
    
    print("moving to min pos")
    servoo.min()
    sleep(1)

    print("moving to mid position")
    servoo.min()
    
    sleep(3)

    servoo.min()

#activate proximity
#ultrasonic = DistanceSensor(echo=17, trigger=3, pin_factory= factory)
# Initial the input pin

def initialInductive(pin): 
  GPIOpin = pin
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(GPIOpin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  print("Finished Initiation")
  print(GPIOpin)
  return GPIOpin

proximity_sensor = initialInductive(26)
object_detected = False

# Detect Object
def detectObject_proximity(pin):
    state = GPIO.input(pin)
    #print(state)
    # 0 --> object detected
    # 1 --> no object
    if state==0:
      print("Object Detected")
      sleep(1)
      return True
    return False




#yolo model
trash_dicc = {'battery': "yellow",
    'can': "blue",
    'cardboard': "blue",
    'drink carton': "yellow",
    'glass bottle': "blue",
    'paper': "blue",
    'plastic bag': "yellow",
    'plastic bottle': "yellow",
    'plastic bottle cap': "yellow",
    'pop tab': "yellow"
}
# apply yolo with my camera
cap = cv2.VideoCapture(0)
model = YOLO('best.pt')
classes = model.names
acc = 0

while True:
    ret, frame = cap.read()
    #acc +=1
    #print(acc)

    #cv2.imshow('frame', frame)
    if detectObject_proximity(proximity_sensor) and not object_detected:
        object_detected = True
        #print("something detected")
        acc = 30 
        

    if object_detected:
        if acc > 1:
            acc-=1
        if acc == 1:
            acc = 0
            #sleep(2)
        
        
            results = model(frame)
            rectangle_thickness = 2
            text_thickness = 2
            highest_probability = 0
            highest_probability_class = ""
            highest_result = None
            box = None
            
            for result in results:
                for box in result.boxes:
                    # get the one with the highest probability
                    if box.conf[0] > highest_probability:
                        highest_probability = box.conf[0]
                        highest_probability_class = result.names[int(box.cls[0])]
                        highest_result = result
            
            if box:
                print(highest_probability_class)
                print(highest_probability)
                bin = trash_dicc[highest_probability_class]
                # Calculate the middle coordinates of the image
                image_height, image_width, _ = frame.shape
                middle_x = int(image_width / 2)
                middle_y = int(image_height / 2)
                
                # Draw rectangle and put text in the middle of the image
                #cv2.rectangle(frame, (int(box.xyxy[0][0]), int(box.xyxy[0][1])),(int(box.xyxy[0][2]), int(box.xyxy[0][3])), (255, 0, 0), rectangle_thickness)
                cv2.putText(frame, f"{bin}",
                            (middle_x, middle_y),
                            cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), text_thickness)
                if bin == "blue":
                    move_servo(servo_1)
                elif bin == "yellow":
                    move_servo(servo_2)
                print(bin)
                sleep(3)
            
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break