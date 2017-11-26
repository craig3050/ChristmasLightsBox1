import RPi.GPIO as GPIO
import threading
from time import sleep
import time
import paho.mqtt.publish as publish
import datetime
import random


# GPIO Ports
Enc_A = 12  # Encoder input A: input GPIO 4
Enc_B = 11  # Encoder input B: input GPIO 14
Enc_C = 16  # Encoder input A: input GPIO 4
Enc_D = 15  # Encoder input B: input GPIO 14

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

def colour_wheel(encoder0Pos):
    encoder0Pos = ((encoder0Pos+1)*(6))
    # Red to yellow
    if (encoder0Pos <= 255):
        colorVal = encoder0Pos
        redVal = 255
        greenVal = colorVal
        blueVal = 0

    # Yellow to green
    elif (encoder0Pos <= 511):
        colorVal = encoder0Pos - 256
        redVal = 255 - colorVal
        greenVal = 255
        blueVal = 0

    # Green to cyan
    elif (encoder0Pos <= 767):
        colorVal = encoder0Pos - 512;
        redVal = 0;
        greenVal = 255;
        blueVal = colorVal;

    # Cyan to blue
    elif (encoder0Pos <= 1023):
        colorVal = encoder0Pos - 768;
        redVal = 0;
        greenVal = 255 - colorVal;
        blueVal = 255;

    # Blue to magenta
    elif (encoder0Pos <= 1279):
        colorVal = encoder0Pos - 1024;
        redVal = colorVal;
        greenVal = 0;
        blueVal = 255;

    # Magenta to red
    else:
        colorVal = encoder0Pos - 1280;
        redVal = 255;
        greenVal = 0;
        blueVal = 255 - colorVal;

    return (redVal,greenVal, blueVal)


def random_effect():
    Number_of_Effects = 18
    effect_0 = "bpm"
    effect_1 = "candy cane"
    effect_2 = "confetti"
    effect_3 = "cyclon rainbow"
    effect_4 = "dots"
    effect_5 = "fire"
    effect_6 = "glitter"
    effect_7 = "juggle"
    effect_8 = "lightning"
    effect_9 = "noise"
    effect_10 = "police all"
    effect_11 = "police one"
    effect_12 = "rainbow"
    effect_13 = "rainbow with glitter"
    effect_14 = "ripple"
    effect_15 = "sinelon"
    effect_16 = "solid"
    effect_17 = "twinkle"

    effect_chosen = random.randrange(1, Number_of_Effects)
    print(effect_chosen)
    if effect_chosen == 0:
        return effect_0
    elif effect_chosen == 1:
        return effect_1
    elif effect_chosen == 2:
        return effect_2
    elif effect_chosen == 3:
        return effect_3
    elif effect_chosen == 4:
        return effect_4
    elif effect_chosen == 5:
        return effect_5
    elif effect_chosen == 6:
        return effect_6
    elif effect_chosen == 7:
        return effect_7
    elif effect_chosen == 8:
        return effect_8
    elif effect_chosen == 9:
        return effect_9
    elif effect_chosen == 10:
        return effect_10
    elif effect_chosen == 11:
        return effect_11
    elif effect_chosen == 12:
        return effect_12
    elif effect_chosen == 13:
        return effect_13
    elif effect_chosen == 14:
        return effect_14
    elif effect_chosen == 15:
        return effect_15
    elif effect_chosen == 16:
        return effect_16
    else:
        return effect_17

def area_name_translation(area_name):
    if area_name == 1:
        return "lights/external/christmas1"
    elif area_name == 2:
        return "lights/external/christmas2"
    elif area_name == 3:
        return "lights/external/christmas3"
    elif area_name == 4:
        return "lights/external/christmas4"
    elif area_name == 5:
        return "lights/external/christmas5"
    elif area_name == 6:
        return "lights/external/christmas6"
    elif area_name == 7:
        return "lights/external/christmas7"
    else:
        return "lights/external/christmas1"

def colour_change(area_name, R, G, B):
    if area_name <= 7:
        area_name1 = area_name_translation(area_name)
        colour = "{\"r\":" + str(R) + ",\"g\":" + str(G) + ",\"b\":" + str(B) + "},\"effect\":\"solid\""
        message = "{\"state\":\"ON\",\"color\":" + colour + "}"
        publish.single(area_name1, message, hostname="192.168.0.14")
    else:
        for i in range(1,7):
            colour_change(i, R, G, B)


def brightness(area_name, brightness):
    if area_name <= 7:
        print("Area Number Recieved" + area_name)
        area_name1 = area_name_translation(area_name)
        message = "{\"state\":\"ON\",\"brightness\":" + str(brightness) + "}"
        publish.single(area_name1, message, hostname="192.168.0.14")
    else:
        for i in range(1, 8):
            print(i)
            brightness(i, brightness)
    return 0

def effect_change(area_name, effect_name):
    if area_name <= 7:
        area_name1 = area_name_translation(area_name)
        effect_name = "\"" + effect_name + "\""
        message = "{\"state\":\"ON\",\"effect\":" + effect_name + "}"
        publish.single(area_name1, message, hostname="192.168.0.14")
    else:
        for i in range(1, 8):
            effect_change(i, effect_name)

def animation_speed(area_name, speed):
    if area_name <= 7:
        area_name1 = area_name_translation(area_name)
        message = "{\"transition\":" + str(speed) + "}"
        publish.single(area_name1, message, hostname="192.168.0.14")
    else:
        for i in range(1, 8):
            animation_speed(i, speed)



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

    Area_Selected = 1 # initial selection of area
    Animation_Speed_to_Colour_Change = 0

    Initial_Counter = 0
    Reset_Counter_Limit = 10000

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
            if Brightness > 254:  # limit Brightness to 0...100
                Brightness = 254
            print(NewCounter1, Brightness)  # some test print
            brightness(Area_Selected, Brightness)

        LockRotary2.acquire()  # get lock for rotary switch
        NewCounter2 = rotary_counter_2  # get counter value
        rotary_counter_2 = 0  # RESET IT TO 0
        LockRotary2.release()  # and release lock

        if (NewCounter2 != 0):  # Counter has CHANGED
            Animation_Speed = Animation_Speed + NewCounter2 * abs(NewCounter2)  # Decrease or increase Brightness
            if Animation_Speed < 0:  # limit Brightness to 0...100
                Animation_Speed = 0
            if Animation_Speed > 254:  # limit Brightness to 0...100
                Animation_Speed = 254
            print(NewCounter2, Animation_Speed)  # some test print
            if Animation_Speed_to_Colour_Change == 1:
                colours = colour_wheel(Animation_Speed)
                red_value = colours[0]
                green_value = colours[1]
                blue_value = colours[2]
                colour_change(Area_Selected, red_value, green_value, blue_value)
            else:
                animation_speed(Area_Selected, Animation_Speed)

        if GPIO.input(33) == False:
            print('Button Pressed 33...')
            Animation_Speed_to_Colour_Change = 1 #flag for changing the function of Animation speed
            Initial_Counter = 0
            time.sleep(0.1)
        elif GPIO.input(31) == False:
            print('Button Pressed 31...')
            Area_Selected = 8
            Initial_Counter = 0
            time.sleep(0.1)
        elif GPIO.input(32) == False:
            print('Button Pressed 32...')
            Area_Selected += 1
            Initial_Counter = 0
            if Area_Selected > 7:
                Area_Selected = 1
            time.sleep(0.1)
        elif GPIO.input(29) == False:
            print('Button Pressed 29...')
            Animation_Speed_to_Colour_Change = 0
            effect = random_effect()
            effect_change(Area_Selected, effect)
            Initial_Counter = 0
            time.sleep(0.1)
        else:
            if Initial_Counter > Reset_Counter_Limit:
                effect = random_effect()
                time.sleep(0.2)
                brightness(8, 254)
                time.sleep(0.2)
                effect_change(8, effect)
                time.sleep(0.2)
                animation_speed(8, 50)
                Initial_Counter = 0
            else:
                Initial_Counter += 1





# start main demo function
main()