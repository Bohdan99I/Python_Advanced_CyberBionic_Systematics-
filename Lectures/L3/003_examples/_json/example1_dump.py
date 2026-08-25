import json

data = {
    'first_name': 'Eugene',
    'last_name': 'Petrov',
    'age': 35,
    'hobbies': [
        'guitar',
        'cars',
        'mountains',
        'adventures'
    ]
}

# конвертація словника у рядок формату JSON
json_data = json.dumps(data)
print(type(json_data))
print(json_data)

# конвертація словника у рядок формату JSON та записом даного тексту у файл.
with open('output.json', 'w') as f:
    # передаємо словник (що хочемо конвертувати в JSON) та файловий дескриптор (куди ходимо записати)
    json.dump(data, f)
