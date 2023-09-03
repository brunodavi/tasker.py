from pytest import MonkeyPatch

from tasker.env import Env


def test_TASKER_PY_PACKAGE_é_uma_variavel_de_ambiente(
    monkeypatch: MonkeyPatch,
):

    monkeypatch.setenv('TASKER_PY_PACKAGE', 'com.taskerpy')

    assert Env().TASKER_PY_PACKAGE == 'com.taskerpy'
