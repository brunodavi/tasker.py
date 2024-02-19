from dataclasses import dataclass
from hashlib import md5

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

    def _generate_id(self, name):
        hash_md5 = md5(name.encode()).hexdigest()
        return int(hash_md5[:7], 16)

    def add_task(
        self,
        name: str | None = None,
        task_id: int | None = None,
        returned: dict[str, str] | None = None,
    ):
        def decorator(action_func):
            task = Task(
                task_id,
                name or action_func.__name__,
                action_func,
                returned,
                self.client,
            )

            if task.id is None:
                task.id = self._generate_id(task.name)

            if not (0 < task.id < 1_000_000_000):
                raise ValueError('Task id invalid min: 0 max: 999_999_999')

            self._tasks.append(task)
            return task

        return decorator
