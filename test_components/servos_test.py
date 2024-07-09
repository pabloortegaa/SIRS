from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory




factory = PiGPIOFactory()

servo_1 = Servo(12, pin_factory=factory)
servo_2 = Servo(2, pin_factory=factory)

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

move_servo(servo_1)
    
    
    




    
    

    


if __name__ == "__main__":
    #servo_2.value = None
    
    #move_servo(servo_1)
    #servo_1.value = None
    
    

    #servo_1.value = None
    move_servo(servo_2)
    #servo_2.value = None



