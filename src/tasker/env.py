from envclass import EnvClass


class Env(EnvClass):
    _prefix = 'TASKER_PY'

    package: str = 'net.dinglisch.android.taskerm'

    address: str = 'localhost'
    port: int = 9170

    timeout: int = 30
