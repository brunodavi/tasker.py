from copy import deepcopy
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Generator

from lxml import etree

from ..task_collision import TaskCollision
from ..xml_utils import XmlUtils
from .action import Action

from httpx import Client

LOCAL_TASKS = '/sdcard/Tasker/tasks/'


@dataclass
class Task:
    id: int
    name: str

    _actions: Callable[..., Generator[Action, None, None]]
    _returned: dict[str, str] | None
    _client: Client

    priority: int = 100
    collision: TaskCollision = TaskCollision.ABORT_NEW_TASK

    par1: Any = None
    par2: Any = None

    variables: dict[str, Any] = field(default_factory=dict)

    def __call__(self, *args, **kwargs):
        for action in self._actions():
            yield deepcopy(action)

    def to_string(self):
        xml_utils = XmlUtils()

        xml_task = xml_utils.create_task(self.id, self.name, *self())

        return etree.tostring(xml_task, pretty_print=True).decode()

    def export(self, directory: str | Path = LOCAL_TASKS):
        filepath = Path(directory) / f'{self.name}.tsk.xml'

        xml_string = self.to_string()
        filepath.write_text(xml_string)
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
