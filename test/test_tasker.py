from dataclasses import dataclass
from pathlib import Path

from pytest import fixture

from tasker.actions.alert import Beep
from tasker.py import Task, TaskerPy


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


def test__generate_id(app: TaskerPy):
    @dataclass
    class Item:
        id: int

    items = [
        Item(1),
        Item(2),
        Item(3),
    ]

    randint_args = [1, 5]

    assert app._generate_id(items, randint_args) in (4, 5)
    assert app._generate_id(items, randint_args) in (4, 5)


def test_iterar_2_vezes_a_mesma_tarefa(app: TaskerPy):
    expected_actions = [
        Beep(frequency=1000, duration=100),
        Beep(frequency=2000, duration=100),
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


def test_converter_para_string(new_task: Task):
    xml_string = new_task.to_string()

    assert isinstance(xml_string, str)


def test_exportar_tarefa(tmp_path: Path, new_task: Task):
    tmp_new_task = new_task.export(tmp_path)
    xml_string = tmp_new_task.read_text()

    assert tmp_new_task.exists()
    assert '<nme>task</nme>' in xml_string
