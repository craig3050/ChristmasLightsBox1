import paho.mqtt.publish as publish
import time

def main():
    brightness = input("Enter Brightness Value to Send: ")
    message = "{\"state\":\"ON\",\"brightness\":" + str(brightness) + "}"
    publish.single("test1", message, hostname="192.168.0.14")


if __name__ == '__main__':
    main()