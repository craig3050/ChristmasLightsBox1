import random


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

def random_effect():
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

def main():
    effect = random_effect()
    print(effect)


if __name__ == '__main__':
    main()