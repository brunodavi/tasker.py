from httpx import Client
from pytest import MonkeyPatch

from tasker.actions.alert import Beep


def mock_post(self, path, json, *args, **kwargs):
    return path, json, self


def test_caminho_do_tasker_client(monkeypatch: MonkeyPatch):
    monkeypatch.setattr(Client, 'post', mock_post)

    beep = Beep()

    expected_data = {
        'frequency': 8000,
        'duration': 1000,
        'amplitude': 50,

        'stream': 3,
    }


    results = beep()

    path = results[0]
    data = results[1]
    client: Client = results[2]

    url = str(client.base_url)

    assert url == 'http://localhost:9170'
    assert path == '/alert/beep'

    assert data == expected_data

