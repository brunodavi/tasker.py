from dataclasses import dataclass
from tasker.py import Action


@dataclass
class SayWaveNet(Action):
    _code_ = 334

    text: str
    voice: str
    stream: int = 3
    pitch: int = 20
    speed: int = 8
    file: str = ''
    override_api_key: str = ''
    respect_audio_focus: bool = True
