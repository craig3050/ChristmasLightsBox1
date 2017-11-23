



def colour_wheel(encoder0Pos):
    encoder0Pos = (encoder0Pos+1)*(6)
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

if __name__ == '__main__':
    colours = colour_wheel()
    red_value = colours[0]
    green_value = colours[1]
    blue_value = colours[2]
    print red_value
    print green_value
    print blue_value
