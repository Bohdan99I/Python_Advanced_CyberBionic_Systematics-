from xml.etree import ElementTree as ET

# відкриваємо файл
tree = ET.parse('data/test.xml')
# отримаємо кореневий DOM-елемент
root = tree.getroot()

# перебираємо усі дочірні елементи
for student_data in root:
    # .attrib- доступ до атрибутів тегу
    print("PK: ", student_data.attrib)
    # ітеруємося по усім внутрішнім тегам та друкуємо назву тегу й контент
    for child in student_data:
        print('{}: {}'.format(child.tag, child.text))

# створюємо корінь та записуємо у нього елементи:
root = ET.Element('record')
for i in range(10):
    sub_element = ET.SubElement(root, 'value{}'.format(i))
    sub_element.text = str(i * 10)

print(ET.dump(root))  # only for dev/trace

data = [
    {'x': 10, 'y': 29, 'z': 90},
    {'x': 11, 'y': 28, 'z': 91},
    {'x': 12, 'y': 27, 'z': 92},
    {'x': 13, 'y': 26, 'z': 93},
    {'x': 14, 'y': 25, 'z': 94},
]

root = ET.Element('records')

for item in data:
    record = ET.SubElement(root, 'record')
    for key, value in item.items():
        e = ET.SubElement(record, key)
        e.text = str(value)

tree = ET.ElementTree(root)
tree.write('data/output.xml', encoding='utf-8')
