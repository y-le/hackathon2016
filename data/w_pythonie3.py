import json
import csv

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

		return (int(degree) + float(minute) / 60 + float(second) / 3600 + float(frac_seconds) / 3600)

dane = []
with open('miejscowosci_zsumowane_dwie.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        #dane.append(dict(zip(header, row)))
        all_data = dict(zip(header, row))

        teryt = all_data['identyfikator jednostki podziału terytorialnego kraju']
        lat = all_data['szerokość geograficzna']
        long = all_data['długość geograficzna']
        name = all_data['nazwa główna']

        datum = {}
        datum['teryt'] = teryt
        datum['lat'] = convert(lat)
        datum['lng'] = convert(long)
        datum['name2'] = name

        #print(teryt + " " + lat + " " + long)
        dane.append(datum)
        #print(datum)

        #print(datum['teryt'] + " " + str(datum['lat']) +  " " + str(datum['long']))


#print(dane)
print(json.dumps(dane, sort_keys=True, indent=4, separators=(',', ': ')))