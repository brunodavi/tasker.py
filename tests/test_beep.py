from tasker.py import TaskerPy

from tasker import Stream
from tasker.actions.alert import Beep


def test_padroes():
    beep = Beep()

    assert beep.frequency == 8000
    assert beep.duration == 1000
    assert beep.amplitude == 50

    assert beep.stream == Stream.MEDIA

