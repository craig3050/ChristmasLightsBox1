#Include list
#MQTT
#Button inputs
import _random

#Global Variables
Area = 1
Brightness = 100
Animation_Speed = 10
Effect = 1
Reset_Counter = 0
Reset_Counter_Limit = 10000
Number_of_Effects = 10


#Pin Allocations
Effect_Button = 1
Area_Button = 2
Animation_Speed_dial = 3
Brightness_dial = 4


def Check_Time():
    #Check time - if between 18:00 and 07:00 (return Y/N)

##there is a better way to do this
def Return_effect(i):
    if i == 1:
        return ("xxx")
    if i > 10:
        return ("solid")

def Transmit(Effect, Area, Animation_Speed, Brightness):
    xxx
#Module 2 - Transmit
#Variables: Area, Effect, Brightness, Animation_Speed
#compile values into JSON string
#If 1-8 transmit one, if 9 loop to transmit values to all.

def Check_Button(Button_Number):
    #debounce

    #return 0 if no press
    #return 1 if pressed + reset_counter = 0

def Check_Dial(Dial_Number):
    #same idea as above
    #reset counter if pressed

def auto_loop();
    for i in enumerate 4: ##check if enumerate is the correct function
        if (Check_Button(i) == 1):
            User_Control()
    elif (Check_Time() == "N"):
        break

    Effect = random(Number_of_Effects)
    Effect_Name = Return_effect(Effect)
    Animation_Speed = random (1,100)
    Area = random (1,9)
    Brightness = 100
    Transmit(Effect, Area, Animation_Speed, Brightness)
#7) wait 1 min (not delay)
#8) Refresh MQTT connection


def User_Control():
    while (Reset_Counter < Reset_Counter_Limit):
        if Check_Dial(1) == 1:
            Brightness += 1
        elif Check_Dial(1) == -1:
            Brightness += -1
        elif Check_Dial (2) == 1:
            Animation_Speed += 1
        elif Check_Dial (2) == -1:
            Animation_Speed += -1
#Buttons (1 = Effect, 2 = Area, 3 = All_Area, 4 = Solid, 5 = Reset
        elif (Check_Button(1) == 1):
            Effect += 1
            Effect_Name = Return_effect(Effect)
        elif (Check_Button(2) == 1):
            Area += 1
            if (Area > 9):
                Area == 1
        elif (Check_Button(3) == 1):
            Area == 9
        elif (Check_Button(4) == 1): ##have a think about how we change animation speed into colour wheel
            Effect_Name = "solid"
        elif (Check_Button(5) == 1):
            break

#I) Transmit values
        Transmit(Effect_Name, Area, Animation_Speed, Brightness)