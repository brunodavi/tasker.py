from tasker.py import Action
from tasker import Stream


class Say(Action):
    def __init__(
        self,
        text = '',
		engine_voice = 'default:default',
		stream = Stream.MEDIA,
		pitch = 5,
		speed = 5,
		respect_focus = True,
		network = False,
		immediately = False
    ):
        self.text = text
        self.engine_voice = engine_voice
        self.stream = stream
        self.pitch = pitch
        self.speed = speed
        self.respect_focus = respect_focus
        self.network = network
        self.immediately = immediately

