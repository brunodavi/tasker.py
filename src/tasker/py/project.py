from dataclasses import dataclass

from tasker.icons import Icon


@dataclass
class Project:
    name: str

    pids: list[int]
    tids: list[int]

    scenes: list[str]

    icon: Icon
