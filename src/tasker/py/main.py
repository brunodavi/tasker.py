from dataclasses import dataclass, field

from .client import TaskerPyClient
from .task import Task
from .scene import Scene


@dataclass
class TaskerPy:
    address: str = 'localhost'
    port: int = 9170

    def __post_init__(self):
        self._client = TaskerPyClient(
            self.address,
            self.port
        )

        self._profiles = []
        self._tasks = []
        self._scenes = []


    def add_task(self, name: str | None = None):
        def decorator(action_func):
            task = Task(
                name or action_func.__name__,
                action_func
            )

            self._tasks.append(task)
            return task

        return decorator
