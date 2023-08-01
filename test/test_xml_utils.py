from lxml import etree

from tasker.xml_utils import XmlUtils
from tasker.actions.alert import Beep


TASK_XML = (
"""
<TaskerData sr="" dvi="1">
	<Task sr="task0">
		<id>0</id>
		<nme>task_test</nme>
		<Action sr="act0" ve="7">
			<code>171</code>
			<Int sr="arg0" val="8000"/>
			<Int sr="arg1" val="1000"/>
			<Int sr="arg2" val="50"/>
			<Int sr="arg3" val="3"/>
			<Str sr="arg4" ve="3"/>
		</Action>
	</Task>
</TaskerData>
"""
)


parser = etree.XMLParser(remove_blank_text=True)


def test_task_xml_creator():
    xml_utils = XmlUtils()

    xml_task = (
        xml_utils
            .create_task(
                0, 'task_test',
                Beep()
            )
    )

    xml_string = etree.tostring(xml_task)

    xml_expected = etree.tostring(
        etree.fromstring(TASK_XML, parser)
    )

    assert xml_string == xml_expected
