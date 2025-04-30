from lxml import etree
from pathlib import Path


MOCK_DIR = 'test/__mocks__'

path_default = Path(MOCK_DIR)


def xml_to_string(element_xml):
    return etree.tostring(element_xml, pretty_print=True, encoding='utf-8').decode()


def read_file(path: Path):
    return path.read_text(encoding='utf8')


def read_xml_task(filename):
    path = path_default / 'tasks'
    path /= filename

    return read_file(path)


def read_xml_profile(filename):
    path = path_default / 'profiles'
    path /= filename

    return read_file(path)


def read_xml_scene(filename):
    path = path_default / 'scenes'
    path /= filename

    return read_file(path)
