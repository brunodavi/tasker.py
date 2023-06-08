from .task import Task

class TaskerPy:
    def add_task(self, name):
        def decorator(task_action):
            task = Task(name)
            task.__call__ = task_action

            return task
        return decorator
