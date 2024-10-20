from enum import IntEnum


class TaskCollision(IntEnum):
    ABORT_NEW_TASK = 0
    ABORT_EXISTING_TASK = 1
    RUN_BOTH_TOGETHER = 2
