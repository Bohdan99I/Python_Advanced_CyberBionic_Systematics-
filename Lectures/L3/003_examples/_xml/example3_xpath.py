from xml.etree import ElementTree as ET

tree = ET.parse('data/test.xml')
root = tree.getroot()

for student_data in root:
    print('PK: ', (student_data.attrib, student_data.get('pk')))
    print('{} {} {}'.format(
        # пошук тегів на першому рівні вкладеності – діти student_data.
        student_data.find('./first_name').text,
        student_data.find('./last_name').text,
        student_data.find('./age').text
    ))

# вибірка всіх тегів first_names із тегів person.
first_names = root.findall('./person/first_name')
# вибірка всіх тегів last_names із тегів person.
last_names = root.findall('./person/last_name')
# вибірка всіх тегів age із тегів person.
ages = root.findall('./person/age')

# збираємо теги у спільні групи та створюємо спільний словник для кожного person.
for values in zip(first_names, last_names, ages):
    row = {value.tag: value.text for value in values}
    print(row)

for student_data in root:
    print("PK: ", student_data.attrib)
    for child in student_data:
        print('{}: {}'.format(child.tag, child.text))
