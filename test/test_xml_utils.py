from lxml import etree

from tasker.actions.alert import Beep, Flash
from tasker.xml_utils import XmlUtils


def read_xml(path):
    parser = etree.XMLParser(remove_blank_text=True)
    mock_tree = etree.parse(path, parser)

    return etree.tostring(mock_tree)


def test_beep_xml_creator():
    expected_xml = read_xml('test/__mocks__/beep.xml')

    xml_utils = XmlUtils()
    xml_task = xml_utils.create_task(1, 'task_test', Beep())
    xml_string = etree.tostring(xml_task)

    assert xml_string == expected_xml


def test_flash_xml_creator():
    expected_xml = read_xml('test/__mocks__/flash.xml')

    xml_utils = XmlUtils()
    xml_task = xml_utils.create_task(1, 'task_test', Flash('text', long=True))
    xml_string = etree.tostring(xml_task)

    assert xml_string == expected_xml
