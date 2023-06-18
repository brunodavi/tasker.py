from dataclasses import dataclass

from tasker.py import Action
from tasker import Stream

@dataclass
class Beep(Action):
    frequency: int = 8000
    duration: int = 1000
    amplitude: int = 50

    stream: int = Stream.MEDIA
