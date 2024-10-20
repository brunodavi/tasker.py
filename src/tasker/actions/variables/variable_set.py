from dataclasses import dataclass

from tasker.py import Action
from tasker.types import Stream


@dataclass
class VariableSet(Action):
    _code_ = 547

    name: str
    to: str
    recurcive: bool = False
    math: bool = False
    append: bool = False
    round: int = 3
    structure: bool = False
    continue_after_error: bool = False
