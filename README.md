# TaskerPy

**TaskerPy** is a tool for creating Android automations using Python, simplifying the integration and control of tasks via Tasker.

## Requirements

- [Python][python-org] v3.10 or higher
- [Tasker][tasker-trial] v6.2 or higher
- The [TaskerPy][tasker-py] project imported in Tasker

## Quick Start

Install directly from GitHub:

```bash
pip install git+https://github.com/brunodavi/tasker.py
```

## Usage Example

Here’s a simple demonstration of how to create an automation with **TaskerPy**:

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

# Play and export the task
hello_world.play()
hello_world.export()  # Exports as XML to /sdcard/Tasker/tasks/Show_Popup.tsk.xml
```

## Contributing

Contributions are welcome! Check the pending tasks on [Projects][gh-projects].

### Setting Up the Environment

We use [PDM][pdm-org] as the package manager. To set up the environment:

```bash
# Install dependencies
pdm install

# Activate the virtual environment
eval $(pdm venv activate)

# On Windows (PowerShell)
Invoke-Expression (pdm venv activate)
```

#### Requirement to lxml
Need `libxml2` and `libxslt`


### Available Scripts

The scripts defined in the `pyproject.toml` include:

- **test**: To run tests.
- **docs**: To generate documentation.
- **lint**: To check code quality.
- **format**: To format the code.

#### Example

```bash
# Run tests
pdm test

# Run tests ignoring Tasker actions
pdm test -k 'not action'
```

## Connecting to Android

If the **tasker.py** project is already imported and running in Tasker, it should work on your phone by default. The default IP is `localhost`.

To run outside the phone, configure the `.env` file with your Android device’s IP:

```env
TASKER_PY_ADDRESS=192.168.1.25
```

## Notes

After importing the project in Tasker, click "Save" (✓), then tap the three dots to exit the editor.

[python-org]: https://www.python.org
[pdm-org]: https://pdm-project.org
[tasker-trial]: https://tasker.joaoapps.com/download.html
[gh-projects]: https://github.com/users/brunodavi/projects/1
[tasker-py]: https://taskernet.com/shares/?user=AS35m8nXHtAHUb3g429CktIgI9aKlA1%2FEglWKHxy0IyPwx0q7aeQMBH2ekF4AG%2F7FRqn58T5R5q3qrGmIPwa&id=Project%3Atasker.py
