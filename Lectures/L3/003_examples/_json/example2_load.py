import json

json_data = '{"first_name": "Eugene"}'
# конвертація рядка формату JSON на словник (dict).
data = json.loads(json_data)
print(data)

with open('output.json', 'r') as f:
    # конвертація рядка формату JSON, який записаний у файлі у словник.
    # полегшує роботу з JSON файлами, щоб не читати вміст самому і не
    # передавати в json.loads, а виконати цю операцію у межах однієї команди.
    data = json.load(f)
    print(type(data))
    print(data)

