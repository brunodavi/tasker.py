import pytest

from tasker.actions.alert import Beep, Flash
from tasker.py import Task, TaskerPy


@pytest.fixture
def add_task_with_return():
    app = TaskerPy()

    variables_returned = {'var': '%par1'}

    return app.add_task('TPY - Run', returned=variables_returned)


def test_beep(add_task_with_return):
    @add_task_with_return
    def task(t: Task):
        t.par1 = 'test_returned'
        yield Beep(1000, duration=100)

    variables = task.play()

    assert isinstance(variables, dict)
    assert variables['var'] == 'test_returned'


def test_flash(add_task_with_return):
    @add_task_with_return
    def task(t: Task):
        t.par1 = 'test_returned'
        yield Flash('Olá, Mundo', long=True)

    variables = task.play()

    assert isinstance(variables, dict)
    assert variables['var'] == 'test_returned'
