from lxml import etree


MOCK_DIR = 'test/__mocks__'


def xml_to_string(element_xml):
    return etree.tostring(element_xml, pretty_print=True, encoding='utf-8').decode()


def read_xml(path):
    parser = etree.XMLParser(remove_blank_text=True)
    mock_tree = etree.parse(path, parser)

    return xml_to_string(mock_tree)


def read_xml_task(name):
    return read_xml(f'{MOCK_DIR}/tasks/{name}')


def read_xml_profile(name):
    return read_xml(f'{MOCK_DIR}/profiles/{name}')


def read_xml_scene(name):
    return read_xml(f'{MOCK_DIR}/scenes/{name}')
