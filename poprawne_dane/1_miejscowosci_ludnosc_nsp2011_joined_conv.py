
csvfile = '1_miejscowosci_ludnosc_nsp2011_joined.csv'
fieldnames = ['nazwa', 'teryt_simc', 'populacja']


def valid_simc(value):
  return len(value) == 7

def parse_teryt(value):
  if len(value) <= 4:
    return value.ljust(6, '0')

ls = []

import csv
with open(csvfile, newline='', encoding='utf-8') as raw:
    reader = csv.reader(raw)
    for row in reader:
        row = dict(zip(fieldnames, row))
        t = parse_teryt(row['teryt_simc'])
        if t: # TERYT line
            teryt = t
            print('TERYT', teryt)
            continue
        assert valid_simc(row['teryt_simc'])
        row['simc'] = row['teryt_simc']
        row['teryt'] = teryt
        row['teryt_simc'] = None
        ls.append(row)

import json
jsonfile = csvfile[:-4] + '.json'
open(jsonfile, 'w', encoding='utf-8').write(json.dumps(ls))

# --- analiza
keys = list((e['teryt'], e['simc'],) for e in ls)

from collections import Counter
print('Is unique?', Counter(keys).most_common(10))

