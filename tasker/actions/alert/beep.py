from tasker.py import Action
from tasker import Stream


class Beep(Action):
    frequency = 8000
    duration = 1000
    amplitude = 50

    stream = Stream.MEDIA
