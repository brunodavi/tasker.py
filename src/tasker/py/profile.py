from dataclasses import dataclass
from .event import Event

@dataclass
class Profile:
    id: int
    task_id: int
    name: str
    event: Event
