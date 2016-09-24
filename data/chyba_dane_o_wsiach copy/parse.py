import csv

import json

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


tab = []


with open('02-table 1.csv') as file:
	for line in file:
		print line.split(';')






#print json.dumps(tab, sort_keys=True, indent=4, separators=(',', ': '))