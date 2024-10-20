from dataclasses import dataclass, field

from tasker.icons import Icon, NoneIcon
from tasker.py import Action
from tasker.types.notify_led import NotifyLed


@dataclass
class Notify(Action):
    _code_ = 523

    title: str
    text: str = ''
    icon: Icon | NoneIcon = NoneIcon()
    number: int = 0
    permanent: bool = False
    priority: int = 3
    repeat_alert: bool = False
    led_colour: NotifyLed = NotifyLed.Red
    led_rate: int = 0
    sound_file: str = ''
    vibration_pattern: str = ''
    category: str = ''
