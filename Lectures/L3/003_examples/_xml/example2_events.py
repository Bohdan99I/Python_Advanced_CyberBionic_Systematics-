from lxml import etree as ET


class PersonTarget:
    """
    Порційна обробка даних файлу XML.
    """

    def __init__(self):
        # визначаємо дефолтні значення перед початком роботи
        self.records = []
        self.current_index = None
        self.current_node = None

    def start(self, tag, attrib):
        # при вході в тег person, додаємо новий запис до списку, яку далі заповнюватимемо у методі data.
        if tag == 'person':
            self.records.append({
                'first_name': '',
                'last_name': '',
                'age': None,
                'metadata': attrib
            })
            self.current_index = len(self.records) - 1
        # вказуємо поточний тег, щоб перевіряти його data.
        self.current_node = tag

    def end(self, tag):
        # після завершення теги скидаємо поточний тег
        self.current_node = ''

    def data(self, data):
        # print('Data: {} -> "{}"'.format(self.current_node, data))
        # перевіряємо поточний тег, якщо він є одним з нас, що цікавлять, то беремо дані з тега
        # і записуємо в елемент з індексом self.current_index.
        if self.current_node in ['first_name', 'last_name', 'age']:
            self.records[self.current_index][self.current_node] = data

    def close(self):
        return self.records


# зв'язок парсера з нашим класом обробником - target.
parser = ET.XMLParser(target=PersonTarget())
infile = 'data/test.xml'
results = ET.parse(infile, parser)

for r in results:
    print(r)
