from tasker.py import TaskerPy

from tasker import Stream
from tasker.actions.alert import Beep


def test_padroes():
    beep = Beep()

    assert beep.frequency == 8000
    assert beep.duration == 1000
    assert beep.amplitude == 50

    assert beep.stream == Stream.MEDIA


def test_modifica_atributos_na_definicao():
    beep = Beep(
        frequency=80,
        duration=100,
        amplitude=5,

        stream=Stream.CALL,
    )

    assert beep.frequency == 80
    assert beep.duration == 100
    assert beep.amplitude == 5

    assert beep.stream == Stream.CALL


def test_contexto_de_criacao():
    app = TaskerPy()

    @app.add_task('Task Beep')
    def task_beep():
        beep = Beep()
        result = beep()

        assert result._is_task_creator == True
        assert result.code == 171
        assert result.args == (
            8000,
            1000,
            50,
            3,
            '3',
        )

    task_beep()


def test_fora_do_contexto_de_criacao():
    beep = Beep()
    result = beep()

    assert result['success'] == True
    assert result.success == True
