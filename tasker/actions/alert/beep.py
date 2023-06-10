from tasker.py import Action
from tasker import Stream


class Beep(Action):
    def __init__(
        self,
        frequency = 8000,
        duration = 1000,
        amplitude = 50,

        stream = Stream.MEDIA,
    ):
        self.frequency = frequency
        self.duration = duration
        self.amplitude = amplitude

        self.stream = stream
