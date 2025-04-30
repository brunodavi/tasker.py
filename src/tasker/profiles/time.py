from dataclasses import dataclass

from tasker.py import Event


@dataclass
class Time(Event):
    start_hour: int
    start_minute: int

    end_hour: int
    end_minute: int

    _every_type = None
    _every_value = None

    def every_hour(self, value: int):
        self._every_type = 1
        self._every_value = value

        return self

    def every_minute(self, value: int):
        self._every_type = 2
        self._every_value = value

        return self
