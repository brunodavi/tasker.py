from tasker.actions.alert import Flash


def test_flash_not_error(add_task_with_return):
    @add_task_with_return
    def task():
        yield Flash('Hello, World!')

    task.par1 = 'test_returned'
    variables = task.play()

    assert isinstance(variables, dict)
    assert variables['var'] == 'test_returned'
