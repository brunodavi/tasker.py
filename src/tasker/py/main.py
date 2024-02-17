from dataclasses import dataclass
from time import time

from .profile import Profile
from .scene import Scene
from .task import Task

from tasker.env import Env

from httpx import Client


@dataclass
class TaskerPy:
    address: str = Env.address
    port: int = Env.port

    timeout: int = Env.timeout

    @property
    def client(self):
        return Client(
            base_url=f'http://{self.address}:{self.port}',
            timeout=self.timeout,
        )

    def __post_init__(self):
        self._profiles: list[Profile] = []
        self._tasks: list[Task] = []
        self._scenes: list[Scene] = []

    def add_task(
        self,
        name: str | None = None,
        task_id: int | None = None,
        returned: dict[str, str] | None = None,
    ):
        if task_id is None:
            task_id = int(time())

        def decorator(action_func):
            task = Task(
                task_id,
                name or action_func.__name__,
                action_func,
                returned,
                self.client,
            )

            self._tasks.append(task)
            return task

        return decorator
