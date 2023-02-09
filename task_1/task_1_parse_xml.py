from lxml import etree

tree = etree.parse("persons.xml")
root = tree.getroot()

field1_elements = root.xpath("//name")
for elem in field1_elements:
    print(elem, elem.text)

field2_elements = root.xpath("//age")
for elem in field2_elements:
    print(elem, elem.text)

