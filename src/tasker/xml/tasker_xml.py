from .project_xml import ProjectXml
from .profile_xml import ProfileXml
from .task_xml import TaskXml
from .scene_xml import SceneXml

from .xml_builder import XmlBuilder


class TaskerXml(XmlBuilder):
    def __init__(self, projects = [], profiles = [], tasks = [], scenes = []):
        self.projects = projects
        self.profiles = profiles
        self.tasks = tasks
        self.scenes = scenes

    def to_xml(self):
        return self.E.TaskerData(
            *self.elements_to_xml(self.profiles),
            *self.elements_to_xml(self.projects),
            *self.elements_to_xml(self.tasks),
            *self.elements_to_xml(self.scenes),

            sr='',
            dvi='1'
        )

    def elements_to_xml(self, elements: list):
        if len(elements) == 0: return []

        first_element = elements[0]

        class_name = type(first_element).__name__

        xml_parsers = {
            'Project': ProjectXml,
            'Profile': ProfileXml,
            'Task': TaskXml,
            'Scene': SceneXml,
        }

        xml_parser = xml_parsers[class_name]

        for element in elements:
             yield xml_parser(element).to_xml()
