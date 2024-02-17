from dataclasses import dataclass

from tasker.types import Stream
from tasker.py import Action


@dataclass
class Morse(Action):
    _code_ = 172

    text: str
    frequency: int = 4000
    speed: int = 80
    amplitude: int = 50
    stream: Stream = Stream.MEDIA
