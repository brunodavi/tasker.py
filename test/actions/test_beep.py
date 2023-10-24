from tasker.actions.alert import Beep


def test_beep_not_error(add_task_with_return):
    @add_task_with_return
    def task():
        yield Beep(1000, duration=100)

    task.par1 = 'test_returned'
    variables = task.play()

    assert isinstance(variables, dict)
    assert variables['var'] == 'test_returned'
