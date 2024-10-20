from envclass import EnvClass


class Env(EnvClass):
    """
    Configuration class for TaskerPy environment variables.

    This class defines the settings required to connect to the
    Tasker application. Environment variable keys are formed by
    combining the prefix with attribute names in uppercase. For
    example, the attribute `package` corresponds to the
    environment variable `TASKER_PY_PACKAGE`.

    Attributes:
        _prefix (str): Prefix for environment variable names.
        package (str): Package name of the Tasker application.
        address (str): Address of the Tasker server. Defaults to 'localhost'.
        port (int): Port number for the Tasker server. Defaults to 9170.
        timeout (int): Timeout duration for requests in seconds. Defaults to 30.
    """

    _prefix = 'TASKER_PY'

    package: str = 'net.dinglisch.android.taskerm'

    address: str = 'localhost'
    port: int = 9170

    timeout: int = 30
