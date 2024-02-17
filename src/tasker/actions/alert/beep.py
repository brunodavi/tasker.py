from dataclasses import dataclass

from tasker.types import Stream
from tasker.py import Action


@dataclass
class Beep(Action):
    _code_ = 171

    frequency: int = 8000
    duration: int = 1000
    amplitude: int = 50

    stream: int = Stream.MEDIA

    do_at_time: str = ''
