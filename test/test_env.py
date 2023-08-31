import pytest
from tasker.env import Env


def test_variavel_de_ambiente_do_pacote_tasker(
        monkeypatch: pytest.MonkeyPatch
    ):

    monkeypatch.setenv(
        "TASKER_PY_PACKAGE",
        "com.taskerpy"
    )


    assert Env().TASKER_PY_PACKAGE == "com.taskerpy"
