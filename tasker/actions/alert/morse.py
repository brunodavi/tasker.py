from tasker.py import Action
from tasker import Stream


class Morse(Action):
    def __init__(
        self,
        text = '',
		frequency = 4000,
		speed = 80,
		amplitude = 50,
		stream = Stream.MEDIA
    ):
        self.text = text
        self.frequency = frequency
        self.speed = speed
        self.amplitude = amplitude
        self.stream = stream

