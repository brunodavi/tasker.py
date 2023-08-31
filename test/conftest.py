from os import getenv

import pytest


def pytest_collection_modifyitems(session, config, items):

    android_data = getenv("ANDROID_DATA")
    address = getenv("TASKER_PY_ADDRESS")

    not_is_android = not (android_data or address)

    for item in items:
        if item.nodeid.startswith("test/test_action") and not_is_android:
            item.add_marker(pytest.mark.skip(reason="Não é Android"))
