

import RPi.GPIO as GPIO
import RPi.GPIO as GPIU
import time

GPIO.setmode(GPIO.BCM)
GPIU.setmode(GPIU.BCM)

GPIO.setup(18,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIU.setup(26,GPIU.IN, pull_up_down = GPIU.PUD_UP)

while True:
    eightteenflag=0
    twensixflag=0
    eightteenp=0
    twensixp=0
    
    input_state = GPIO.input(18)
    input_statedos=GPIU.input(26)

    #statedos -> 26
    #state ->18
    
    if input_state == False and twensixp == 0 :
        print("Entraria una persona")
        eightteenflag=1
        eightteenp=1
        twensixp=99
        time.sleep(1)
        if input_statedos == False and twensixp== 99 and eightteenp==1:
            print("Entro la persona")   
    
    elif input_statedos == False and eightteenp==0:
        print("Se supone saldria 1 persona")
        twensixflag=1
        twensixp=1
        eightteenflag=99
        time.sleep(1)
        if input_state == False and twensixp== 1 and eightteenp==99:
            print("Salio la persona")
    time.sleep(0.2)
'''
    if etp==1 and tsp==3 and tsflag==1 and etflag==1: #if etflag == 1 and tsflag == 1 and etp==1 :
        print("Entro 1 persona")
    elif tsp==1 and etp==3 and tsflag==1 and etflag==1: #etflag==1 and tsflag == 1 and tsp==1 :
        print("Salio 1 persona")'''

