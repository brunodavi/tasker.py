from os import getenv

from pytest import Function, mark, fixture

from tasker.py import TaskerPy


@fixture
def add_task_with_return():
    app = TaskerPy()

    variables_returned = {'var': '%par1'}

    return app.add_task('TPY - Run', returned=variables_returned)
