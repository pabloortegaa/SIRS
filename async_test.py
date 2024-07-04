import asyncio
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


async def waiting(led_pin):
    GPIO.setup(led_pin, GPIO.OUT)
    for i in range(0,5):
        print(f"LED {led_pin} on")
        GPIO.output(led_pin, GPIO.HIGH)
        await asyncio.sleep(0.5)
        print(f"LED {led_pin} off")
        GPIO.output(led_pin, GPIO.LOW)
        await asyncio.sleep(0.5)

async def main():

    blue_pin = 4
    yellow_pin = 14
    brown_pin = 17
    green_pin = 22
    white_pin = 23
    
    # Creating tasks for each LED
    tasks = [
        asyncio.create_task(waiting(blue_pin)),
        asyncio.create_task(waiting(yellow_pin)),
        asyncio.create_task(waiting(brown_pin)),
        asyncio.create_task(waiting(white_pin)),
        asyncio.create_task(waiting(green_pin))
    ]
    
    # Running the tasks concurrently
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        GPIO.cleanup()
