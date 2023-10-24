from envclass import EnvClass


class Env(EnvClass):
    """
    Carrega as variáveis de ambiente esxistentes
    com informações do Tasker
    """

    _prefix = 'TASKER_PY'
    _strict = False

    version: str
    package: str = 'net.dinglisch.android.taskerm'

    address: str = 'localhost'
    port: int = 9170

    timeout: int = 30
