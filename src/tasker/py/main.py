from dataclasses import dataclass
from os import getenv
from random import randint

from .client import TaskerPyClient
from .profile import Profile
from .scene import Scene
from .task import Task


@dataclass
class TaskerPy:
    address: str = getenv("TASKER_PY_ADDRESS") or "localhost"
    port: int = 9170

    def __post_init__(self):
        self._client = TaskerPyClient(
            self.address,
            self.port
        )

        self._profiles: list[Profile] = []
        self._tasks: list[Task] = []
        self._scenes: list[Scene] = []

    def _generate_id(
            self,
            items: list[Profile] | list[Task] | list[Scene],
            randint_args = [1_000, 100_000],
        ) -> int:
        new_id = randint(*randint_args)

        if any((new_id == item.id for item in items)):
            return self._generate_id(items, randint_args)

        return new_id


    def add_task(
            self,
            name: str | None = None,
            task_id: int = None,
            returned: dict[str, str] = None
        ):
        if task_id is None:
            task_id = self._generate_id(self._tasks)

        def decorator(action_func):
            task = Task(
                task_id,
                name or action_func.__name__,
                action_func,
                returned,
                self._client,
            )

            self._tasks.append(task)
            return task

        return decorator
