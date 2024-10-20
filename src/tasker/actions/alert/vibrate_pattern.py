from dataclasses import dataclass

from tasker.py import Action


@dataclass
class VibratePattern(Action):
    _code_ = 62
    pattern: str = '50,100,50,100'
