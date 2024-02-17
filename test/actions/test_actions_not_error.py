from pathlib import Path
from pytest import fixture, FixtureRequest

from tasker.actions.alert import (
    Beep,
    Notify,
    VibratePattern,
    Vibrate,
    Torch,
    ShutUp,
    SayToFile,
    Say,
    Flash,
    Morse,
    NotifyCancel,
)

from tasker.py import Action


@fixture(
    params=[
        Beep(8000, duration=100),
        VibratePattern('0,10'),
        Vibrate(10),
        Torch(),
        Say('Hello, World!', speed=1, immediately=True),
        ShutUp(),
        SayToFile('f', filename='audio', speed=100),
        Flash('Smoke Test!'),
        Morse('a', speed=100),
        Notify('title'),
        NotifyCancel('title'),
    ]
)
def alert_action(request: FixtureRequest):
    yield request.param
    Path('audio.wav').unlink(missing_ok=True)


def test_alert_actions(add_task_with_return, alert_action: Action):
    @add_task_with_return
    def task():
        yield alert_action

    task.par1 = 'test_returned'
    variables = task.play()

    assert isinstance(variables, dict)
    assert variables['var'] == 'test_returned'
