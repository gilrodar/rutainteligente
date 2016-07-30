import time
import time

import RPi.GPIO as GPIO
import RPi.GPIO as GPIU
GPIO.setmode(GPIO.BCM)
GPIU.setmode(GPIU.BCM)
GPIU.setup(26, GPIU.IN, pull_up_down=GPIU.PUD_UP)

GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    input_state=GPIO.input(18)
    input_statedos=GPIU.input(26)
    if input_statedos == False:
        print("Button 26  pressed")
        time.sleep(0.3)
    if input_state== False:
        print("Button pressed 18")
        time.sleep(0.2)


