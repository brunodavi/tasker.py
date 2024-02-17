from dataclasses import dataclass

from tasker.py import Action


@dataclass
class NotifyCancel(Action):
    _code_ = 779

    title: str = ''
