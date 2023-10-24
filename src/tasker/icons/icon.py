from dataclasses import asdict, dataclass

from tasker.env import Env


env = Env()

TASKER_PY_PACKAGE = env.package


@dataclass
class Icon(str):
    package: str = TASKER_PY_PACKAGE

    def __post_init__(self):
        res = f'android.resource://{self.package}/drawable'

        for attr, icon in asdict(self).items():
            setattr(self, attr, f'{res}/{icon}')
