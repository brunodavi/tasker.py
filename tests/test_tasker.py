from tasker.py import TaskerPy


def test_contexto_de_criacao():
    app = TaskerPy()

    @app.add_task('Task Beep')
    def task_beep():


def test_fora_do_contexto_de_criacao():
    beep = Beep()
    result = beep()

    assert result['success'] == True
    assert result.success == True
