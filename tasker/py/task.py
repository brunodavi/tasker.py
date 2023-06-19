from dataclasses import dataclass, field
from typing import Any

from .action import Action
from ..task_collision import TaskCollision

@dataclass
class Task:
    name: str

    collision: TaskCollision = (
        TaskCollision.ABORT_NEW_TASK
    )

    par1: Any = None
    par2: Any = None

    variables: dict[str, Any] = field(default_factory=dict)

    actions: list[Action] = field(default_factory=list)


    def __call__(self, *args, **kwargs):
        ...


    def add_action(self, action: Action):
        self.actions.append(action)

