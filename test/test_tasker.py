from dataclasses import dataclass
from pathlib import Path

from pytest import fixture, raises

from tasker.py import Action, Task, TaskerPy


@dataclass
class ActionTest(Action):
    _code_ = 1

    value: int = 0


@fixture
def app():
    return TaskerPy()


@fixture
def actions():
    return [
        ActionTest(1),
        ActionTest(2),
        ActionTest(3),
    ]


@fixture
def task_no_name(app: TaskerPy):
    @app.add_task()
    def task():
        yield ActionTest(1)
        yield ActionTest(2)
        yield ActionTest(3)

    return task


@fixture
def task_with_name(app: TaskerPy):
    @app.add_task(name='Task Name')
    def task():
        yield ActionTest(3)
        yield ActionTest(2)
        yield ActionTest(1)

    return task


def test_task_no_name(task_no_name: Task):
    assert isinstance(task_no_name, Task)
    assert task_no_name.name == 'task'


def test_task_with_name(task_with_name: Task):
    assert isinstance(task_with_name, Task)
    assert task_with_name.name == 'Task Name'


def task_actions_in_task(task_no_name: Task, task_with_name: Task, actions):
    assert [*task_no_name()] == actions
    assert [*task_with_name()] == reversed(actions)


def test_id_limit(app: TaskerPy):
    @app.add_task(task_id=int('9' * 9))
    def task1():
        ...

    with raises(ValueError):

        @app.add_task(task_id=int('-' + ('9' * 9)))
        def task2():
            ...

    with raises(ValueError):

        @app.add_task(task_id=int('9' * 10))
        def task3():
            ...


def test_iter_task(task_no_name: Task, actions):
    assert [*task_no_name()] == actions
    assert [*task_no_name()] == actions


def test_convert_to_string(task_no_name: Task):
    xml_string = task_no_name.to_string()

    assert isinstance(xml_string, str)
    assert '<nme>task</nme>' in xml_string


def test_export_task(tmp_path: Path, task_no_name: Task):
    tmp_task_exported = task_no_name.export(tmp_path)
    xml_string = tmp_task_exported.read_text()

    assert tmp_task_exported.exists()
    assert tmp_path == tmp_task_exported.parent

    assert '<nme>task</nme>' in xml_string


def test_export_file_task(tmp_path: Path, task_no_name: Task):
    tmp_path /= 'task.xml'
    tmp_task_exported = task_no_name.export(tmp_path)
    xml_string = tmp_task_exported.read_text()

    assert tmp_task_exported.exists()
    assert tmp_path == tmp_task_exported

    assert '<nme>task</nme>' in xml_string


def test_stores_tasks(app: TaskerPy):
    @app.add_task()
    def task1():
        ...

    @app.add_task()
    def task2():
        ...

    @app.add_task()
    def task3():
        ...

    assert app._tasks == [
        task1,
        task2,
        task3,
    ]


def test_client():
    app = TaskerPy(
        address='0.0.0.0',
        port=8080,
        timeout=15,
    )

    assert str(app.client.base_url) == 'http://0.0.0.0:8080'
    assert app.client.timeout.read == 15
