import paho.mqtt.publish as publish
import time

area_name = "test1"
effect_name = "rainbow"

def colour_change(area_name, R, G, B):
    colour = "{\"r\":" + str(R) + ",\"g\":" + str(G) + ",\"b\":" + str(B) + "},\"effect\":\"solid\""
    message = "{\"state\":\"ON\",\"color\":" + colour + "}"
    publish.single(area_name, message, hostname="192.168.0.14")

def brightness(area_name, brightness):
    message = "{\"state\":\"ON\",\"brightness\":" + str(brightness) + "}"
    publish.single(area_name, message, hostname="192.168.0.14")

def effect_change(area_name, effect_name):
    effect_name = "\"" + effect_name + "\""
    message = "{\"state\":\"ON\",\"effect\":" + effect_name + "}"
    publish.single(area_name, message, hostname="192.168.0.14")

def main():
    bright_value = input("Enter Brightness Value to Send: ")
    brightness(area_name, bright_value)
    R = input("Enter R: ")
    G = input("Enter G: ")
    B = input("Enter B: ")
    colour_change(area_name, R, G, B)
    effect_change(area_name, effect_name)


if __name__ == '__main__':
    main()
