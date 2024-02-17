from tasker.actions.alert import Notify
from tasker.icons.misc import Misc


def test_notify_not_error(add_task_with_return):
    @add_task_with_return
    def task():
        yield Notify('title', icon=Misc.STAR)

    task.par1 = 'test_returned'
    variables = task.play()

    assert isinstance(variables, dict)
    assert variables['var'] == 'test_returned'
