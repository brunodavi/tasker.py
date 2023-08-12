from pytest import fixture

from tasker.py import TaskerPy, Task
from tasker.actions.alert import Beep


@fixture
def app():
    return TaskerPy()


def test_criar_tarefa_e_ações(app: TaskerPy):
    expected_actions = [
        Beep(1000, duration=100),
        Beep(2000, duration=100),
        Beep(3000, duration=100),
        Beep(4000, duration=100),
    ]


    @app.add_task('Task Name')
    def task(t: Task):
        beep = Beep(1000, duration=100)
        yield beep

        for _ in range(3):
            beep.frequency += 1000
            yield beep


    assert isinstance(task, Task)
    assert task.name == 'Task Name'

    assert len(app.tasks) == 1
    assert [*task()] == expected_actions


def test_iterar_2_vezes_a_mesma_tarefas(app: TaskerPy):
    expected_actions = [
        Beep(frequency=1000, duration=100),
        Beep(frequency=2000, duration=100)
    ]

    @app.add_task(name='2_task')
    def task2_iters(t: Task):
        yield Beep(frequency=1000, duration=100)
        yield Beep(frequency=2000, duration=100)

    assert [*task2_iters()] == expected_actions
    assert [*task2_iters()] == expected_actions


def test_criar_tarefa_sem_nome(app):
    app = TaskerPy()

    @app.add_task()
    def task(t: Task):
        yield Beep(duration=100)

    assert isinstance(task, Task)
    assert task.name == 'task'

    assert len(app.tasks) == 1
