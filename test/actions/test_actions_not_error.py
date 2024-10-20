from pathlib import Path

from pytest import FixtureRequest, fixture

from tasker.actions.alert import (
    Beep,
    Flash,
    Morse,
    Notify,
    NotifyCancel,
    Say,
    SayToFile,
    ShutUp,
    Torch,
    Vibrate,
    VibratePattern,
)
from tasker.actions.variables import VariableSet
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


@fixture(
    params=[
        VariableSet('%var', 'value'),
    ]
)
def variables_action(request: FixtureRequest):
    yield request.param


def test_alert_actions(add_task_with_return, alert_action: Action):
    @add_task_with_return
    def task():
        yield alert_action

    task.par1 = 'test_returned'
    variables = task.play()

    assert isinstance(variables, dict)
    assert variables['var'] == 'test_returned'


def test_variables_actions(add_task_with_return, variables_action: Action):
    @add_task_with_return
    def task():
        yield variables_action

    task.par1 = 'test_returned'
    variables = task.play()

    assert isinstance(variables, dict)
    assert variables['var'] == 'test_returned'
