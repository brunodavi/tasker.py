from os import getenv

from pytest import Function, fixture, mark

from tasker.actions.alert import Beep, Flash, Notify
from tasker.profiles.time import Time
from tasker.py import TaskerPy, Profile


@fixture
def app():
    return TaskerPy()


@fixture
def add_task_with_return():
    app = TaskerPy()

    variables_returned = {'var': '%par1'}

    return app.add_task('TPY - Run', output_variables=variables_returned)


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

@fixture
def time_profile(beep_task):
    app = TaskerPy()

    profile_creator = app.add_profile(
        'Profile Time',
        Time(12, 0, 20, 0).every_hour(2),
        profile_id=1,
    )

    return profile_creator(beep_task)
