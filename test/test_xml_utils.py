from lxml import etree

from tasker.actions.alert import Beep, Flash
from tasker.xml_utils import XmlUtils

BEEP_XML = """
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

FLASH_XML = """
<TaskerData sr="" dvi="1">
	<Task sr="task">
		<cdate>0</cdate>
		<edate>1</edate>
		<id>1</id>
		<nme>task_test</nme>
		<pri>100</pri>
		<Action sr="act0" ve="7">
			<code>548</code>
			<Str sr="arg0" val="text"/>
			<Int sr="arg1" val="1"/>
			<Int sr="arg2" val="0"/>
			<Str sr="arg3" val=""/>
			<Str sr="arg4" val=""/>
			<Str sr="arg5" val=""/>
			<Str sr="arg6" val=""/>
			<Str sr="arg7" val=""/>
			<Str sr="arg8" val=""/>
			<Int sr="arg9" val="1"/>
            <Str sr="arg10" val=""/>
			<Int sr="arg11" val="1"/>
			<Int sr="arg12" val="0"/>
			<Str sr="arg13" val=""/>
			<Int sr="arg14" val="0"/>
			<Str sr="arg15" val=""/>
		</Action>
	</Task>
</TaskerData>
"""

parser = etree.XMLParser(remove_blank_text=True)


def test_beep_xml_creator():
    xml_utils = XmlUtils()
    xml_task = xml_utils.create_task(1, 'task_test', Beep())
    xml_string = etree.tostring(xml_task)

    xml_expected = etree.tostring(etree.fromstring(BEEP_XML, parser))

    assert xml_string == xml_expected


def test_flash_xml_creator():
    xml_utils = XmlUtils()
    xml_task = xml_utils.create_task(1, 'task_test', Flash('text', long=True))

    xml_string = etree.tostring(xml_task)

    xml_expected = etree.tostring(etree.fromstring(FLASH_XML, parser))

    assert xml_string == xml_expected
