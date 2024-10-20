from dataclasses import dataclass

@dataclass
class Element:
    ...


@dataclass
class Size:
    width: int
    height: int


@dataclass
class Scene:
    name: str

    portatil: Size
    landscape: Size

    elements: list[Element]
