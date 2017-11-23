import datetime
import time


def main():
    now = datetime.datetime.now()

    if now.hour <= 7:
        print ("programme will run")
    elif now.hour >=18:
        print ("programme will run")
    else:
        print ("programme will NOT run")
        time.sleep(1)
    return 0

if __name__ == '__main__':
    main()
