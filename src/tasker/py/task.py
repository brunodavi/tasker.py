from copy import copy
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Generator

from lxml import etree

from tasker.task_collision import TaskCollision

from tasker.icons.icon import Icon
from tasker.py.action import Action
from tasker.py.profile_variable import ProfileVariable
from tasker.xml.tasker_xml import TaskerXml

from httpx import Client


@dataclass
class Task:
    id: int
    name: str

    _actions: Callable[..., Generator[Action, None, None]]
    _returned: dict[str, str] | None
    _client: Client

    priority: int = 100
    collision: TaskCollision = TaskCollision.ABORT_NEW_TASK

    awake: bool = False
    notify: bool = False

    profile_variables: list[ProfileVariable] = field(default_factory=list)

    
    par1: Any = None
    par2: Any = None

    variables: dict[str, Any] = field(default_factory=dict)

    icon: Icon | None = None

    def __call__(self, *args, **kwargs):
        for action in self._actions():
            yield copy(action)

    def to_string(self):
        task_xml = TaskerXml(tasks=[self])
        return task_xml.to_string()

    def export(self, directory: str | Path = '/sdcard/Tasker/tasks/'):
        filepath = Path(directory)

        if filepath.is_dir():
            filepath /= f'{self.name}.tsk.xml'

        TaskerXml(tasks=[self]).export(filepath)
        return filepath

    def play(self):
        body = {
            'task_xml': self.to_string(),
            'task_name': self.name,
            'par1': self.par1,
            'par2': self.par2,
            'response_schema': {
                'status_code': 200,
                'headers': 'host:tasker.py',
                'body': self._returned,
            },
        }

        return self._client.post('/run', json=body).json()
