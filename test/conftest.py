from os import getenv

from pytest import Function, mark, fixture

from tasker.py import TaskerPy


@fixture
def add_task_with_return():
    app = TaskerPy()

    variables_returned = {'var': '%par1'}

    return app.add_task('TPY - Run', returned=variables_returned)


def pytest_collection_modifyitems(session, config, items: list[Function]):
    ANDROID_DATA = getenv('ANDROID_DATA')
    TASKER_PY_ADDRESS = getenv('TASKER_PY_ADDRESS')

    android_connected = not (ANDROID_DATA or TASKER_PY_ADDRESS)

    for item in items:
        if item.nodeid.startswith('test/actions/test_') and android_connected:
            item.add_marker(mark.skip(reason='Android not connected'))
