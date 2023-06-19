from enum import Enum
from os import getenv


class Env(str, Enum):
    def __str__(self):
        return getenv(self.value)

    TASKER_PY_PACKAGE = 'TASKER_PY_PACKAGE'
