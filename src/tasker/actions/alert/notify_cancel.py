from tasker.py import Action


class NotifyCancel(Action):
    def __init__(self, title=None, warn_not_exist=False):
        self.title = title
        self.warn_not_exist = warn_not_exist
