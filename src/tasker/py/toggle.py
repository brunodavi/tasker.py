from dataclasses import dataclass

from tasker.py import Action


@dataclass
class Toggle(Action):
    """Block to build on/off actions."""

    on: bool = False

    def toggle(self):
        self.on = not self.on
        return self
