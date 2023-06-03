from tasker.py import TaskerPy
from tasker.actions.alert import Beep


def test_contexto_de_criacao():
    app = TaskerPy()
    beep = Beep()

    @app.add_task('Task Name')
    def task():
        beep()

    task()

    assert beep.create_action.called()


def test_fora_do_contexto_de_criacao():
    beep = Beep()
    beep()

    assert beep.take_action.called()
