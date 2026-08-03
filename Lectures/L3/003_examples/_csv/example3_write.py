import csv

with open('data/output.csv', 'w') as f:
    # екранування значень лише за потребою, якщо вони містять символи, які порушують парсинг. Наприклад: "", ",", etc.
    writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
    writer.writerow(['1', '2', '3'])
