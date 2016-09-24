import csv

import json

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


tab = []


with open('02-table 1.csv') as file:
	for line in file:
		split = line.split(';')
		if (len(split) >= 14 and split[1].isdigit and len(split[1]) == 7):
			#print split[0], split[1], split[2]

			datum = {}
			datum['name'] = split[0]
			datum['teryt'] = split[1]
			datum['population'] = split[2]
			print datum











#print json.dumps(tab, sort_keys=True, indent=4, separators=(',', ': '))