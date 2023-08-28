from lxml import etree

from tasker.xml_utils import XmlUtils
from tasker.actions.alert import Beep


TASK_XML = (
"""
<TaskerData sr="" dvi="1">
	<Task sr="task">
		<cdate>0</cdate>
		<edate>1</edate>
		<id>1</id>
		<nme>task_test</nme>
		<pri>100</pri>
		<Action sr="act0" ve="7">
			<code>171</code>
			<Int sr="arg0" val="8000"/>
			<Int sr="arg1" val="1000"/>
			<Int sr="arg2" val="50"/>
			<Int sr="arg3" val="3"/>
			<Str sr="arg4" val=""/>
		</Action>
	</Task>
</TaskerData>
"""
)


parser = etree.XMLParser(remove_blank_text=True)


def test_task_xml_creator():
    xml_utils = XmlUtils()
    xml_task = xml_utils.create_task(1, 'task_test', Beep())
    xml_string = etree.tostring(xml_task)

    xml_expected = etree.tostring(
        etree.fromstring(TASK_XML, parser)
    )

    assert xml_string == xml_expected
