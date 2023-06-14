from tasker.py import Task, Action


class Notify(Action):
    def __init__(
        self,
        title = '',
		text = ' ',
		icon = ' ',
		permanent = False,
		priority = 3,
		repeat_alert = False,
		sound_file = None,
		vibration_pattern = None,
		category = None
    ):
        self.title = title
        self.text = text
        self.icon = icon
        self.permanent = permanent
        self.priority = priority
        self.repeat_alert = repeat_alert
        self.sound_file = sound_file
        self.vibration_pattern = vibration_pattern
        self.category = category

    def add_button1(label: str, task: Task): ...
