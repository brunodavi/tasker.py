from enum import Enum


class Stream(int, Enum):
    """
    Opção de saida de áudio do dispositivo

    Examples:
        >>> Stream.ALARM
    """

    CALL = 0
    SYSTEM = 1
    RINGER = 2
    MEDIA = 3
    ALARM = 4
    NOTIFICATION = 5
