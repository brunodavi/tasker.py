from .xml_builder import XmlBuilder


class SceneXml(XmlBuilder):
    def __init__(self, scene):
        self.scene = scene
