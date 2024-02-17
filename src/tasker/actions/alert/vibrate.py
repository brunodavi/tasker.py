from dataclasses import dataclass

from tasker.py import Action


@dataclass
class Vibrate(Action):
    _code_ = 61
    time: int = 200
