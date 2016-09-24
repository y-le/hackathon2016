import json
import csv

dane = []
with open('miejscowosci_zsumowane_dwie.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        dane.append(dict(zip(header, row)))

print(json.dumps(dane))