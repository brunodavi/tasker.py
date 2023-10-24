from dataclasses import dataclass
from random import randint

from .profile import Profile
from .scene import Scene
from .task import Task

from tasker.env import Env

from httpx import Client


env = Env()

TASKER_PY_ADDRESS = env.address
TASKER_PY_PORT = env.port

TASKER_PY_TIMEOUT = env.timeout


@dataclass
class TaskerPy:
    address: str = TASKER_PY_ADDRESS
    port: int = TASKER_PY_PORT

    timeout: int = TASKER_PY_TIMEOUT

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

    def _generate_id(
        self,
        items: list[Profile] | list[Task] | list[Scene],
        randint_args=[1_000, 100_000],
    ) -> int:
        new_id = randint(*randint_args)

        if any((new_id == item.id for item in items)):
            return self._generate_id(items, randint_args)

        return new_id

    def add_task(
        self,
        name: str | None = None,
        task_id: int | None = None,
        returned: dict[str, str] | None = None,
    ):
        if task_id is None:
            task_id = self._generate_id(self._tasks)

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
