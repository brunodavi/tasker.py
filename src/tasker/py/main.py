from dataclasses import dataclass
from hashlib import md5

from httpx import Client

from tasker.env import Env

from .profile import Profile
from .project import Project
from .scene import Scene
from .task import Task

from .event import Event


@dataclass
class TaskerPy:
    """
    Represents the main interface for TaskerPy, managing connection settings, projects, profiles, tasks and scenes.

    Attributes:
        address (str): The IP address of the Tasker server. Default is taken from environment variables.
        port (int): The port number used for the Tasker server. Default is from environment variables.
        timeout (int): The request timeout value in seconds. Default is from environment variables.
    """

    address: str = Env.address
    port: int = Env.port
    timeout: int = Env.timeout

    @property
    def client(self):
        """
        Creates a new HTTP client for communicating with the Tasker server.

        Returns:
            Client (Client): An HTTP client configured with the Tasker server's base URL and timeout settings.
        """
        return Client(
            base_url=f'http://{self.address}:{self.port}',
            timeout=self.timeout,
        )

    def __post_init__(self):
        """
        Initializes internal storage for projects, profiles, tasks, and scenes after the class is instantiated.
        """
        self._projects: list[Project] = []
        self._profiles: list[Profile] = []
        self._tasks: list[Task] = []
        self._scenes: list[Scene] = []

    def _generate_id(self, name: str) -> int:
        """
        Generates a unique task ID using the MD5 hash of the task name.

        Args:
            name (str): The name of the task for which to generate an ID.

        Returns:
            int: A unique task ID derived from the hash of the task name.
        """
        hash_md5 = md5(name.encode()).hexdigest()
        return int(hash_md5[:7], 16)

    def add_profile(
        self,
        name: str,
        event: Event,
        profile_id: int = None
    ):
        def decorator(task: Task):
            profile = Profile(
                profile_id,
                task.id,
                name,
                event
            )

            if profile.id is None:
                profile.id = self._generate_id(name)

            if not (0 < profile.id < 1_000_000_000):
                raise ValueError('Profile id invalid min: 0 max: 999_999_999')

            self._profiles.append(profile)
            return profile

        return decorator

    def add_task(
        self,
        name: str = None,
        task_id: int = None,
        output_variables: dict[str, str] = None,
    ):
        """
        Decorator to add a task to the TaskerPy application.

        Args:
            name (str, optional): The name of the task. If not provided, defaults to the function name.
            task_id (int, optional): A specific task ID. If not provided, a unique ID will be generated.
            output_variables (dict[str, str], optional): A dictionary mapping Python variable names to Tasker variable names.

        Examples:
            >>> from tasker.py import TaskerPy
            >>> from tasker.actions.variables import VariableSet
            >>>
            >>> app = TaskerPy()
            >>>
            >>> @app.add_task(name='My Task', task_id=12300, output_variables={'var_python': '%VarTasker'})
            ... def my_task():
            ...     yield VariableSet('%VarTasker', 'Hello, World!')
            >>>
            >>> my_task.play()
            >>> {'var_python': 'Hello, World!'}

        Returns:
            Task (Task): Wrapped with the TaskerPy.

        Raises:
            ValueError: If the task ID is invalid (must be between 1 and 999,999,999).
        """

        def decorator(action_func):
            task = Task(
                task_id,
                name or action_func.__name__,
                action_func,
                output_variables,
                self.client,
            )

            if task.id is None:
                task.id = self._generate_id(task.name)

            if not (0 < task.id < 1_000_000_000):
                raise ValueError('Task id invalid min: 0 max: 999_999_999')

            self._tasks.append(task)
            return task

        return decorator
