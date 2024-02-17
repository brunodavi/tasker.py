from dataclasses import dataclass
from tasker.py import Toggle


@dataclass
class Torch(Toggle):
    _code_ = 511

    level: str = ''
