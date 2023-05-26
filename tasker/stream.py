from enum import Enum

class Stream(int, Enum):
    CALL = 0
    SYSTEM = 1
    RINGER = 2
    MEDIA = 3
    ALARM = 4
    NOTIFICATION = 5

