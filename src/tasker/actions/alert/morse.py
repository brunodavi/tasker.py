from dataclasses import dataclass

from tasker import Stream
from tasker.py import Action


@dataclass
class Morse(Action):
    text: str
    frequency: int = 4000
    speed: int = 80
    amplitude: int = 50
    stream: Stream = Stream.MEDIA
