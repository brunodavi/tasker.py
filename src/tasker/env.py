from dataclasses import asdict, dataclass
from os import getenv


@dataclass
class Env:
    TASKER_PY_PACKAGE: str = ""
    TASKER_PY_ADDRESS: str = ""
    TASKER_VERSION: str = ""

    def __post_init__(self):
        for attr in asdict(self):
            env_var = getenv(attr)
            setattr(self, attr, env_var)
