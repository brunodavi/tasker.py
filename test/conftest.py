from os import getenv

from pytest import mark, Function


def pytest_collection_modifyitems(session, config, items: list[Function]):

    ANDROID_DATA = getenv('ANDROID_DATA')
    TASKER_PY_ADDRESS = getenv('TASKER_PY_ADDRESS')

    not_is_android = not (ANDROID_DATA or TASKER_PY_ADDRESS)

    for item in items:
        if item.nodeid.startswith('test/test_action') and not_is_android:
            item.add_marker(mark.skip(reason='Não é Android'))