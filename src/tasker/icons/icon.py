from dataclasses import asdict, dataclass

from ..app_info import AppInfo


@dataclass
class Icon(str):
    def __post_init__(self):
        res = AppInfo.RESOURCE.value

        for attr, icon in asdict(self).items():
            setattr(self, attr, f'{res}/{icon}')
