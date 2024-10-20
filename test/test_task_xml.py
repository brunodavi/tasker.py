from lxml import etree
from pytest import fixture

from tasker.py.profile_variable import ProfileVariable
from tasker.xml import TaskerXml


def xml_to_string(element_xml):
    etree.tostring(element_xml, pretty_print=True, encoding='utf-8').decode()


def read_xml(path):
    parser = etree.XMLParser(remove_blank_text=True)
    mock_tree = etree.parse(path, parser)

    return xml_to_string(mock_tree)


def test_beep_xml(beep_task):
    expected_xml = read_xml('test/__mocks__/beep.xml')

    task_xml = TaskerXml(tasks=[beep_task]).to_xml()
    xml_string = xml_to_string(task_xml)
    assert xml_string == expected_xml


def test_flash_xml(flash_task):
    expected_xml = read_xml('test/__mocks__/flash.xml')

    task_xml = TaskerXml(tasks=[flash_task]).to_xml()
    xml_string = xml_to_string(task_xml)
    assert xml_string == expected_xml


def test_task_profile_variable(flash_task):
    expected_xml = read_xml('test/__mocks__/flash_profile_variables.xml')

    flash_task.profile_variables = [
        ProfileVariable(variable_name='%test_variable', value='TEST_VALUE'),
        ProfileVariable(
            config_type='n',
            config_on_imported=True,
            structure_variable=True,
            immutable=True,
            variable_name='%foo',
            value='30',
            display='Value',
            prompt='Message',
            same_value=False,
            exported_value='-1',
        ),
    ]

    task_xml = TaskerXml(tasks=[flash_task]).to_xml()
    xml_string = xml_to_string(task_xml)
    assert xml_string == expected_xml
