import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    num_attributes = 0
    for child in node.iter():
        num_attributes += len(child.attrib)
    return num_attributes

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))