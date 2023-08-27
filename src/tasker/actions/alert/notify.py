from dataclasses import dataclass

from tasker.py import Action

@dataclass
class Notify(Action):
    title: str
    text: str = None
    icon: str = None
    permanent: bool = False
    priority: int = 3
    repeat_alert: bool = False
    sound_file: str = None
    vibration_pattern: str = None
    category: str = None
