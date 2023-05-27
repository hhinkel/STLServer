import datetime
import time


def countdown(minutes=5):
    total_seconds = minutes * 60
    while total_seconds > 0:
        timer = datetime.timedelta(seconds=total_seconds)
        print(timer, "/r")
        time.sleep(1)
        total_seconds -= 1
    while True:
        timer = datetime.timedelta(seconds=total_seconds)
        print(timer, "/r")
        time.sleep(1)
        total_seconds += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    countdown(1)
