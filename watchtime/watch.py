from ast import While
from datetime import datetime
from time import sleep
from os import system
from os import name as os_name

def clear():
    system("clear" if os_name == "posix" else "cls")

class WatchTime:
    def __init__(self, hour, minute):
        self.hour = (hour + (minute // 60)) % 24
        self.minute = minute % 60

    def __eq__(self, other):
        if not isinstance(other, WatchTime):
            return False
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, other):
        if not isinstance(other, WatchTime):
            return NotImplemented
        return WatchTime(self.hour + other.hour, self.minute + other.minute)

    def __sub__(self, other):
        if not isinstance(other, WatchTime):
            return NotImplemented
        return WatchTime(0, (self.hour * 60 + self.minute) - (other.hour * 60 + other.minute))


    def __lt__(self, other):
        if not isinstance(other, WatchTime):
            return NotImplemented
        return (self.hour, self.minute) < (other.hour, other.minute)

    def __gt__(self, other):
        if not isinstance(other, WatchTime):
            return NotImplemented
        return (self.hour, self.minute) > (other.hour, other.minute)

    def __le__(self, other):
        if not isinstance(other, WatchTime):
            return NotImplemented
        return (self.hour, self.minute) <= (other.hour, other.minute)

    def __ge__(self, other):
        if not isinstance(other, WatchTime):
            return NotImplemented
        return (self.hour, self.minute) >= (other.hour, other.minute)

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"


def RealTimeWatchTime(hour=0, minute=0):
    now = datetime.now()
    return WatchTime(now.hour + hour, now.minute + minute)

def TimeZone(zonehour, zoneminute=0):
    return RealTimeWatchTime() + WatchTime(zonehour, zoneminute)

def WithDateTime(dt):
    return WatchTime(dt.hour, dt.minute)

def TodayDate(fmt="%d.%m.%Y"):
    now = datetime.now()
    return now.strftime(fmt)

def AtThatMoment(action, *args, **kwargs):
    while True:
        try:
            clear()
            print(action(*args, **kwargs))
            sleep(1)
        except KeyboardInterrupt:
            print("\nThe execution thread has been stopped!")
            break
