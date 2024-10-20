from os import getenv

from pytest import Function, mark, fixture

from tasker.py import TaskerPy
from tasker.actions.alert import Flash, Beep


@fixture
def app():
    return TaskerPy()


@fixture
def add_task_with_return():
    app = TaskerPy()

    variables_returned = {'var': '%par1'}

    return app.add_task('TPY - Run', returned=variables_returned)


@fixture
def beep_task():
    app = TaskerPy()

    @app.add_task()
    def task_beep():
        yield Beep()

    return task_beep


@fixture
def flash_task():
    app = TaskerPy()

    @app.add_task()
    def task_flash():
        yield Flash('Hello, World')

    return task_flash
