import socket


def parse_http_response(text_response):
    # розбиваємо відповідь на окремі рядки
    lines = text_response.split('\n')
    # розділяємо рядок статусу та заголовки/контент
    status_raw, lines = lines[0], lines[1:]
    # розділяємо рядок статусу, розділяючи protocol, status code, message
    # Приклад рядка: `HTTP/1.1 200 OK`
    protocol, status_code, message = status_raw.split(' ')
    # запускаємо цикл, для проходу по всіх заголовках та пошуку рядка контенту
    empty_index = 1
    headers = {}
    for index, line in enumerate(lines):
        # видаляємо всі порожні символи \r та пробіли
        line = line.strip()
        line = line.strip('\r')
        # перевіряємо, чи є рядок порожнім
        if line == '':
            # якщо рядок порожній, то ми дійшли до контенту і нам треба
            # запам'ятати індекс, з якого починається контент і завершити цикл.
            empty_index = index
            break
        print(line)
        # у випадку, якщо ми не дійшли до контенту, то ми все ще знаходимося
        # на блоці із заголовками - розбиваємо заголовки за символом `:` і
        # зберігаємо у словник назву та значення заголовка.
        k, _, v = line.partition(':')
        headers.setdefault(k.strip(), v.strip())
    # індекс порожнього рядка – empty_index.
    # для взяття контенту, треба використовувати всі рядки нижче
    # порожній - empty_index + 1
    content = ''.join(lines[empty_index + 1:])
    # повертаємо відповідь у вигляді кортежу:
    # (status_code: int, headers: dict, content: str)
    return int(status_code), headers, content


# створюємо TCP-сокет (IP) та підключаємося до домену
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('example.com', 80))
content_items = [
    'GET / HTTP/1.1',
    'Host: example.com',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
]
content = '\n'.join(content_items)
print('--- HTTP MESSAGE ---')
print(content)
print('--- END OF MESSAGE ---')
sock.send(content.encode())
result = sock.recv(10024)
# спроба вручну обробити відповідь від http-сервера, розпаривши заголовки та контент
status_code, headers, content = parse_http_response(result.decode())
print('\n')
print('Status Code: {}'.format(status_code))
print('Headers: {}'.format(headers))
print('Content:')
print(content)
