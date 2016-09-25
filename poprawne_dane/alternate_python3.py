import json
import csv
from decimal import Decimal

def convert(x):
	if (len(x) == 10):
		degree = x[0:2]
		minute = x[3:5]
		second = x[6:8]
		#frac_seconds = 0
		if (not degree.isdigit()):
			return False
		if (not minute.isdigit()):
			return False
		if (not second.isdigit()):
			return False

		frac_seconds = 0

		return str(Decimal(degree) + Decimal(minute) / 60 + Decimal(second) / 3600 + Decimal(frac_seconds) / 3600)

dane = []

with open('miejscowosci-prng2.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        all_data = dict(zip(header, row))
        for key in ["szerokość geograficzna","długość geograficzna"]:
          all_data[key] = convert(all_data[key])
        dane.append(all_data)


print(json.dumps(dane, sort_keys=True, indent=4, separators=(',', ': ')))
