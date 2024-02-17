from dataclasses import dataclass

from tasker.py import Action


@dataclass(order=True)
class SayToFile(Action):
    _code_ = 699

    text: str
    engine: str = "default:default"
    filename: str = ''
    pitch: int = 5
    speed: int = 5
    network: bool = True
    immediately: bool = False
    continue_after_error: bool = False

    def __post_init__(self):
        if not self.filename:
            raise ValueError('Arguments "filename" and "text" is required!')
        self.filename += '.wav'
