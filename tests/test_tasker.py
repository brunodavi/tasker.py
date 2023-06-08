from tasker.py import TaskerPy, Task
from tasker.actions.alert import Beep


def test_criar_tarefa():
    app = TaskerPy()
    beep = Beep()

    @app.add_task('Task Name')
    def task():
        beep.add_action()

    assert isinstance(task, Task)
    assert task.name == 'Task Name'
