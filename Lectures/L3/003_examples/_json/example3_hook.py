import datetime
import json


class DateFormatEncoder(json.JSONEncoder):
    """
    Описуємо клас для конвертації дати та часу у формат JSON,
    тут використовується свій власний формат вигляду:
    {
        "value": "01/02/1990 12:57:31",
        "__date__": true
    }
    """

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return {
                'value': obj.strftime('%d/%m/%Y %H:%M:%S'),
                '__datetime__': True
            }
        elif isinstance(obj, datetime.date):
            return {
                'value': obj.strftime('%d/%m/%Y'),
                '__date__': True
            }
        # викликаємо стандартну конвертацію, якщо obj не date або datetime
        return json.JSONEncoder.default(self, obj)


data = {
    'first_name': 'Eugene',
    'last_name': 'Petrov',
    'birthday': datetime.date(1986, 9, 29),
    'hired_at': datetime.datetime(2006, 9, 29, 12, 30, 5),
    'hobbies': [
        'guitar',
        'cars',
        'mountains',
        'adventures'
    ]
}

# використовуємо ключовий аргумент cls зі значенням нашого класу.
# indent=4 - використовується 4 пробіли для форматування JSON
json_data = json.dumps(data, cls=DateFormatEncoder, indent=4)
print(json_data)

with open('output.json', 'w') as f:
    json.dump(data, f, cls=DateFormatEncoder)


def as_date_datetime(dct):
    """
    Функція для зворотного конвертації date та datetime з JSON у внутрішні
    типи Python.

    {
        "value": "01/02/1990 12:57:31",
        "__date__": true
    }
    to datetime(1990, 2, 1, 12, 57, 31)

    и

    {
        "value": "01/02/1990",
        "__date__": true
    }
    to date(1990, 2, 1)
    """
    print(dct)
    if '__datetime__' in dct:
        return datetime.datetime.strptime(dct['value'], '%d/%m/%Y %H:%M:%S')
    if '__date__' in dct:
        return datetime.datetime.strptime(dct['value'], '%d/%m/%Y').date()
    return dct


with open('output.json', 'r') as f:
    # використовуємо ключовий аргумент object_hook для передачі нашої функції
    data = json.load(f, object_hook=as_date_datetime)
    print(data)
