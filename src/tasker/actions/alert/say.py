from dataclasses import dataclass

from tasker.py import Action
from tasker.types import Stream


@dataclass
class Say(Action):
    _code_ = 559

    text: str
    engine_voice: str = 'default:default'
    stream: int = Stream.MEDIA
    pitch: int = 5
    speed: int = 5
    respect_focus: bool = True
    network: bool = True
    immediately: bool = False
