from .xml_builder import XmlBuilder


class ProjectXml(XmlBuilder):
    def __init__(self, project):
        self.project = project
