from dataclasses import dataclass, field
from typing import Any, Callable, Generator
from copy import deepcopy

from .action import Action
from ..task_collision import TaskCollision


@dataclass
class Task:
    name: str
    actions: Callable[..., Generator[Action, None, None]]

    priority: int = 100
    collision: TaskCollision = (
        TaskCollision.ABORT_NEW_TASK
    )

    par1: Any = None
    par2: Any = None

    variables: dict[str, Any] = field(default_factory=dict)


    def __call__(self, *args, **kwargs):
        for action in self.actions(self):
            yield deepcopy(action)

