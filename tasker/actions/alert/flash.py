from tasker.py import Action


class Flash(Action):
    def __init__(
        self,
        text = '',
        long = False,
        immediately = True,
    ):
        self.text = text
        self.long = long
        self.immediately = immediately
