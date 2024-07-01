import time
import RPi.GPIO as GPIO

# Pin of Input
#GPIOpin = -1

# Initial the input pin
def initialInductive(pin):
  global GPIOpin 
  GPIOpin = pin
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(GPIOpin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  print("Finished Initiation")
  print(GPIOpin)

# Detect Object
def detectObject():
    state = GPIO.input(GPIOpin)
    #print(state)
    # 0 --> object detected
    # 1 --> no object
    if state==0:
      print("Object Detected")
      time.sleep(1)


# test module
if __name__ == '__main__':
  pin = 26
  initialInductive(pin)
  while True:
    detectObject()
    #time.sleep(0.1)


