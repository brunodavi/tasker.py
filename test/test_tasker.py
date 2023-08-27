from tempfile import NamedTemporaryFile
from pytest import fixture

from tasker.py import TaskerPy, Task
from tasker.actions.alert import Beep


@fixture
def app():
    return TaskerPy()


@fixture
def new_task(app: TaskerPy):
    @app.add_task()
    def task(t: Task):
        yield Beep(duration=100)
        yield Beep(duration=200)
        yield Beep(duration=300)

    return task


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

    assert len(app._tasks) == 1
    assert [*task()] == expected_actions


def test_iterar_2_vezes_a_mesma_tarefa(app: TaskerPy):
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


def test_criar_tarefa_sem_nome(app: TaskerPy):
    @app.add_task()
    def task(t: Task):
        yield Beep(duration=100)

    assert isinstance(task, Task)
    assert task.name == 'task'
    assert [*task()] == [Beep(duration=100)]

    assert len(app._tasks) == 1


def test_exportar_tarefa(new_task: Task):
    with NamedTemporaryFile('w') as tmp:
        assert new_task.export(tmp.name) is int

def test_converter_para_string(new_task: Task):
    assert new_task.to_string() is str
