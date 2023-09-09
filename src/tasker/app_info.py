from enum import Enum

from .env import Env


class AppInfo(str, Enum):
    """
    Mostra informações do aplicativo Tasker

    Examples:
        >>> AppInfo.PACKAGE
        'net.dinglisch.android.taskerm'
    """
    PACKAGE = 'net.dinglisch.android.taskerm' or Env().TASKER_PY_PACKAGE

    RESOURCE = f'android.resource://{PACKAGE}/drawable'
