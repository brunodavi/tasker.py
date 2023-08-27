from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Generator
from copy import deepcopy

from lxml import etree

from ..xml_utils import XmlUtils
from .action import Action
from ..task_collision import TaskCollision


LOCAL_TASKS = '/sdcard/Tasker/tasks/'


@dataclass
class Task:
    name: str
    actions: Callable[..., Generator[Action, None, None]]

    priority: int = 100
    collision: TaskCollision = (
        TaskCollision.ABORT_NEW_TASK
    )

    par1: Any = None
    par2: Any = None

    variables: dict[str, Any] = field(default_factory=dict)


    def __call__(self, *args, **kwargs):
        for action in self.actions(self):
            yield deepcopy(action)

    def to_string(self):
        xml_utils = XmlUtils()

        xml_task = xml_utils.create_task(
            self.name,
            *self()
        )

        return etree.tostring(xml_task)

    def export(self, diretory = LOCAL_TASKS):
        filepath = (
            Path(diretory) / f'{self.name}.tsk.xml'
        )

        xml_string = self.to_string()
        return filepath.write_text(xml_string)
