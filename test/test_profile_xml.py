from tasker.xml import TaskerXml

from test.helpers.xml_reader import (
    read_xml_profile,
    xml_to_string
)

from test.helpers.str_exporter import tmp_export_str


def test_time_xml(time_profile, beep_task):
    expected_xml = read_xml_profile('time.xml')

    xml = TaskerXml(
        profiles=[time_profile],
        tasks=[beep_task],
    ).to_xml()

    xml_string = xml_to_string(xml)

    tmp_export_str('time_exported.xml', xml_string)

    assert xml_string == expected_xml
