# TaskerPy
**TaskerPy** is a tool for creating Android automations using Python, simplifying the integration and control of tasks via Tasker.

## Installation
`{{ commands.install }}`

## Quick Start

Here’s a simple demonstration of how to create an automation with **TaskerPy** from **Android**:

```python
from tasker.py import TaskerPy, Task
from tasker.actions.alert import Flash as Toast, Beep

app = TaskerPy()

# Displays a message and plays three beeps
@app.add_task(name='Show Popup')
def hello_world():
    yield Toast('Hello, World', long=True)
    yield Beep(frequency=8_000, duration=100)
    yield Beep(frequency=9_000, duration=100)
    yield Beep(frequency=10_000, duration=100)

# Imports the task and executes it
hello_world.play()
hello_world.export()  # Exports as XML to /sdcard/Tasker/tasks/Show_Popup.tsk.xml
```
