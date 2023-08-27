from dataclasses import dataclass

from tasker.py import Action
from tasker import Stream


@dataclass
class Say(Action):
    text: str = ''
    engine_voice: str = 'default:default'
    stream: Stream = Stream.MEDIA
    pitch: int = 5
    speed: int = 5
    respect_focus: bool = True
    network: bool = False
    immediately: bool = False
