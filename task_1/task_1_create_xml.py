import xml.etree.ElementTree as ET

root = ET.Element("root")
persons = ET.SubElement(root, "persons")
teacher = ET.SubElement(persons, "teacher")
student = ET.SubElement(persons, "student")
teacher_name = ET.SubElement(teacher, "name").text = "Bob"
teacher_age = ET.SubElement(teacher, "age").text = "43"
student_name = ET.SubElement(student, "name").text = "Jim"
student_age = ET.SubElement(student, "age").text = "17"

tree = ET.ElementTree(root)
tree.write("persons.xml")

