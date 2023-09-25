from dataclasses import dataclass

from tasker.py import Action


@dataclass
class Flash(Action):
    _code_ = 548

    text: str
    long: bool = False

    layout: bool = False

    title: str = ''
    icon: str = ''
    icon_size: str = ''
    background_colour: str = ''
    task: str = ''
    timeout: str = ''
    immediately: bool = True
    text_color: str = ''
    hide_on_click: bool = True
    show_all: bool = False
    position: str = ''
    use_html: bool = False
    id: str = ''
