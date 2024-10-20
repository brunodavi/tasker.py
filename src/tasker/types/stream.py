from enum import IntEnum


class Stream(IntEnum):
    CALL = 0
    SYSTEM = 1
    RINGER = 2
    MEDIA = 3
    ALARM = 4
    NOTIFICATION = 5
