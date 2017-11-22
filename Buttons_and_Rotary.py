import RPi.GPIO as GPIO
import threading
from time import sleep
import time

# GPIO Ports
Enc_A = 16  # Encoder input A: input GPIO 4
Enc_B = 15  # Encoder input B: input GPIO 14
Enc_C = 12  # Encoder input A: input GPIO 4
Enc_D = 11  # Encoder input B: input GPIO 14


rotary_counter_1 = 0  # Start counting from 0
rotary_counter_2 = 0  # Start counting from 0
Current_A = 1  # Assume that rotary switch is not
Current_B = 1  # moving while we init software
Current_C = 1  # Assume that rotary switch is not
Current_D = 1  # moving while we init software

LockRotary1 = threading.Lock()  # create lock for rotary switch
LockRotary2 = threading.Lock()  # create lock for rotary switch

# initialize interrupt handlers
def init():
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BOARD)  # Use BCM mode
    # define the Encoder switch inputs
    GPIO.setup(Enc_A, GPIO.IN)
    GPIO.setup(Enc_B, GPIO.IN)
    GPIO.setup(Enc_C, GPIO.IN)
    GPIO.setup(Enc_D, GPIO.IN)
    # setup callback thread for the A and B encoder
    # use interrupts for all inputs
    GPIO.add_event_detect(Enc_A, GPIO.RISING, callback=rotary_interrupt1)  # NO bouncetime
    GPIO.add_event_detect(Enc_B, GPIO.RISING, callback=rotary_interrupt1)  # NO bouncetime
    GPIO.add_event_detect(Enc_C, GPIO.RISING, callback=rotary_interrupt2)  # NO bouncetime
    GPIO.add_event_detect(Enc_D, GPIO.RISING, callback=rotary_interrupt2)  # NO bouncetime

    # Buttons setup
    GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    return


# Rotarty encoder interrupt:
# this one is called for both inputs from rotary switch (A and B)
def rotary_interrupt1(A_or_B):
    global rotary_counter_1, Current_A, Current_B, LockRotary1
    # read both of the switches
    Switch_A = GPIO.input(Enc_A)
    Switch_B = GPIO.input(Enc_B)
    # now check if state of A or B has changed
    # if not that means that bouncing caused it
    if Current_A == Switch_A and Current_B == Switch_B:  # Same interrupt as before (Bouncing)?
        return  # ignore interrupt!

    Current_A = Switch_A  # remember new state
    Current_B = Switch_B  # for next bouncing check

    if (Switch_A and Switch_B):  # Both one active? Yes -> end of sequence
        LockRotary1.acquire()  # get lock
        if A_or_B == Enc_B:  # Turning direction depends on
            rotary_counter_1 += 1  # which input gave last interrupt
        else:  # so depending on direction either
            rotary_counter_1 -= 1  # increase or decrease counter
        LockRotary1.release()  # and release lock
    return  # THAT'S IT

# Rotarty encoder interrupt:
# this one is called for both inputs from rotary switch (C and D)
def rotary_interrupt2(C_or_D):
    global rotary_counter_2, Current_C, Current_D, LockRotary2
    # read both of the switches
    Switch_C = GPIO.input(Enc_C)
    Switch_D = GPIO.input(Enc_D)
    # now check if state of A or B has changed
    # if not that means that bouncing caused it
    if Current_C == Switch_C and Current_D == Switch_D:  # Same interrupt as before (Bouncing)?
        return  # ignore interrupt!

    Current_C = Switch_C  # remember new state
    Current_D = Switch_D  # for next bouncing check

    if (Switch_C and Switch_D):  # Both one active? Yes -> end of sequence
        LockRotary2.acquire()  # get lock
        if C_or_D == Enc_D:  # Turning direction depends on
            rotary_counter_2 += 1  # which input gave last interrupt
        else:  # so depending on direction either
            rotary_counter_2 -= 1  # increase or decrease counter
        LockRotary2.release()  # and release lock
    return  # THAT'S IT



# Main loop. Demonstrate reading, direction and speed of turning left/rignt
def main():
    global rotary_counter_1, LockRotary1, rotary_counter_2, LockRotary2

    Brightness = 0  # Current Brightness
    NewCounter1 = 0  # for faster reading with locks

    Animation_Speed = 0  # Current Brightness
    NewCounter2 = 0  # for faster reading with locks

    init()  # Init interrupts, GPIO, ...

    while True:  # start test
        sleep(0.1)  # sleep 100 msec

        # because of threading make sure no thread
        # changes value until we get them
        # and reset them

        LockRotary1.acquire()  # get lock for rotary switch
        NewCounter1 = rotary_counter_1  # get counter value
        rotary_counter_1 = 0  # RESET IT TO 0
        LockRotary1.release()  # and release lock

        if (NewCounter1 != 0):  # Counter has CHANGED
            Brightness = Brightness + NewCounter1 * abs(NewCounter1)  # Decrease or increase Brightness
            if Brightness < 0:  # limit Brightness to 0...100
                Brightness = 0
            if Brightness > 100:  # limit Brightness to 0...100
                Brightness = 100
            print NewCounter1, Brightness  # some test print


        LockRotary2.acquire()  # get lock for rotary switch
        NewCounter2 = rotary_counter_2  # get counter value
        rotary_counter_2 = 0  # RESET IT TO 0
        LockRotary2.release()  # and release lock

        if (NewCounter2 != 0):  # Counter has CHANGED
            Animation_Speed = Animation_Speed + NewCounter2 * abs(NewCounter2)  # Decrease or increase Brightness
            if Animation_Speed < 0:  # limit Brightness to 0...100
                Animation_Speed = 0
            if Animation_Speed > 100:  # limit Brightness to 0...100
                Animation_Speed = 100
            print NewCounter2, Animation_Speed  # some test print
            
            

        if GPIO.input(33) == False:
            print('Button Pressed 33...')
            time.sleep(0.1)
        elif GPIO.input(31) == False:
            print('Button Pressed 31...')
            time.sleep(0.1)
        elif GPIO.input(32) == False:
            print('Button Pressed 32...')
            time.sleep(0.1)
        elif GPIO.input(29) == False:
            print('Button Pressed 29...')
            time.sleep(0.1)
# start main demo function
main()