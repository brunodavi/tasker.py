from tasker.py import TaskerPy, Task
from tasker.actions.alert import Beep


def test_criar_tarefa_e_ações():
    app = TaskerPy()

    @app.add_task('Task Name')
    def task(t: Task):
        beep = Beep(1000, duration=100)
        t.add_action(beep)

        for _ in range(3):
            beep.frequency += 1000
            t.add_action(beep)


    assert isinstance(task, Task)
    assert task.name == 'Task Name'

    assert len(task.actions) == 4
    assert len(app.tasks) == 1

def test_criar_tarefa_sem_nome():
    app = TaskerPy()

    @app.add_task()
    def task(t: Task):
        t.add_action(
            Beep(duration=100)
        )

    assert isinstance(task, Task)
    assert task.name == 'task'

    assert len(task.actions) == 1
    assert len(app.tasks) == 1
