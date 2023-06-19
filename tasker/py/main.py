from dataclasses import dataclass, field

from .client import TaskerPyClient

from .profile import Profile
from .task import Task
from .scene import Scene


@dataclass
class TaskerPy:
    address: str = 'localhost'
    port: int = 9170

    client: TaskerPyClient | None = None

    profiles: list[Profile] = field(default_factory=list)
    tasks: list[Task] = field(default_factory=list)
    scenea: list[Scene] = field(default_factory=list)


    def __post_init__(self):
        self.client = TaskerPyClient(
            self.address,
            self.port
        )

    def add_task(self, name: str):
        def decorator(func):
            task = Task(name)
            func(task)

            self.tasks.append(task)
            return task

        return decorator
