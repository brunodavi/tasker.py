from enum import Enum


class TaskCollision(int, Enum):
    ABORT_NEW_TASK = 0
    ABORT_EXISITING_TASK = 1
    RUN_BOTH_TOGETHER = 2
