from .xml_builder import XmlBuilder


class ProfileXml(XmlBuilder):
    def __init__(self, profile):
        self.profile = profile
