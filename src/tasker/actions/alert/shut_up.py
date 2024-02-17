from dataclasses import dataclass

from tasker.py import Action


@dataclass
class ShutUp(Action):
    _code_ = 697
