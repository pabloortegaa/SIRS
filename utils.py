from time import sleep
import RPi.GPIO as GPIO
import cv2
from ultralytics import YOLO
from inference_sdk import InferenceHTTPClient
import asyncio


## PROXIMITY SENSOR FUNCTIONS ##


def initialInductive(pin): 
  GPIOpin = pin
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(GPIOpin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  #print("Finished Initiation")
  #print(GPIOpin)
  return GPIOpin



# Detect Object
def detectObject_proximity(pin):
    state = GPIO.input(pin)
    #print(state)
    # 0 --> object detected
    # 1 --> no object
    if state==0:
      print("Object Detected")
    
      return True
    else:
        return False


## YOLO FUNCTION ##

def apply_yolo(image): 

    trash_dicc = {'BIODEGRADABLE': "brown",
                    'CARDBOARD': "blue",
                    "CLOTH": "blue",
                    "GLASS": "blue",
                    "METAL": "yellow",
                    "PAPER": "blue",
                    "PLASTIC": "yellow"
    }

    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="edaGCjsVTBNpdktOlNxH"
    )

    trash_class = ""
    result = CLIENT.infer(image, model_id="garbage-classification-3/2")
    if result["predictions"] != []:
        max_pred = max(result["predictions"], key=lambda x: x["confidence"])
        print(max_pred)
        trash_class = trash_dicc[max_pred['class']]
    
    
    return trash_class

## LEDS FUNCTIONS ##


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def turn_led_on(led_pin): 
    GPIO.setup(led_pin ,GPIO.OUT)
    print("LED on")
    GPIO.output(led_pin,GPIO.HIGH)




def turn_led_off(led_pin):
    GPIO.setup(led_pin ,GPIO.OUT)
    print("LED off")
    GPIO.output(led_pin,GPIO.LOW)



async def waiting(led_pin):
    GPIO.setup(led_pin, GPIO.OUT)
    for i in range(0,5):
        print(f"LED {led_pin} on")
        GPIO.output(led_pin, GPIO.HIGH)
        await asyncio.sleep(0.5)
        print(f"LED {led_pin} off")
        GPIO.output(led_pin, GPIO.LOW)
        await asyncio.sleep(0.5)



    


