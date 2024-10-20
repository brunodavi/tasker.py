from pathlib import Path

from lxml import etree
from lxml.builder import E, ElementMaker


class XmlBuilder:
    E: ElementMaker = E

    def to_xml(self) -> ElementMaker:
        ...

    def read_xml(self, path: Path | str):
        parser = etree.XMLParser(remove_blank_text=True)
        return etree.parse(path, parser)

    def to_string(self):
        element_xml = self.to_xml()
        return etree.tostring(
            element_xml, pretty_print=True, encoding='utf-8'
        ).decode()

    def export(self, path: Path | str):
        xml_text = self.to_string()
        path = str(path)

        return Path(path).write_text(xml_text)
