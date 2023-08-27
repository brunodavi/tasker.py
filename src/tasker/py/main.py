from typing import Iterable, Callable
from dataclasses import astuple, dataclass, field


from .client import TaskerPyClient

from .profile import Profile
from .task import Task
from .scene import Scene

from .action import Action


@dataclass
class TaskerPy:
    address: str = 'localhost'
    port: int = 9170

    client: TaskerPyClient | None = None

    profiles: list[Profile] = field(default_factory=list)
    tasks: list[Task] = field(default_factory=list)
    scenea: list[Scene] = field(default_factory=list)


    def __post_init__(self):
        if not self.client:
            self.client = TaskerPyClient(
                self.address,
                self.port
            )


    def add_task(self, name: str | None = None):
        def decorator(action_func):
            task = Task(
                name or action_func.__name__,
                action_func
            )

            self.tasks.append(task)
            return task

        return decorator
    


