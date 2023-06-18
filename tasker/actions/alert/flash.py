from dataclasses import dataclass

from tasker.py import Action


@dataclass
class Flash(Action):
    text: str
    long: bool = False
    immediately: bool = True
