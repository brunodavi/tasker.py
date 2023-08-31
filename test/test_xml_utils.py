from pathlib import Path
from re import sub

from lxml import etree
from tasker.actions.alert import Beep
from tasker.xml_utils import XmlUtils


def test_task_xml_creator():
    xml_expected = Path("test/__mock__/task.xml").read_text()
    xml_expected = sub(r"[\n\t]", "", xml_expected).encode()

    xml_utils = XmlUtils()
    xml_task = xml_utils.create_task(1, "task_test", Beep())
    xml_string = etree.tostring(xml_task)

    assert xml_string == xml_expected
