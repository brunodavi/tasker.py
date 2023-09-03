from tasker.actions.alert import Beep
from tasker.py import Task, TaskerPy


def test_beep():
    app = TaskerPy()

    variables_returned = {'var': r'%par1'}

    @app.add_task('TPY - Run', returned=variables_returned)
    def task(t: Task):
        t.par1 = 'test_returned'
        yield Beep(1000, duration=100)

    variables = task.play()

    assert isinstance(variables, dict)
    assert variables['var'] == 'test_returned'
