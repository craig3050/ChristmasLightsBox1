import paho.mqtt.publish as publish
import time

def colour_change(R, G, B):
    colour = "{\"r\":" + str(R) + ",\"g\":" + str(G) + ",\"b\":" + str(B) + ",\"effect\":\"solid\"}"
    message = "{\"state\":\"ON\",\"color\":" + colour + "}"
    publish.single("test1", message, hostname="192.168.0.14")

def brightness(brightness):
    message = "{\"state\":\"ON\",\"brightness\":" + str(brightness) + "}"
    publish.single("test1", message, hostname="192.168.0.14")

def effect_change(effect_name):
    print("none")

def main():
    bright_value = input("Enter Brightness Value to Send: ")
    brightness(bright_value)
    R = input("Enter R: ")
    G = input("Enter G: ")
    B = input("Enter B: ")
    colour_change(R, G, B)


if __name__ == '__main__':
    main()
