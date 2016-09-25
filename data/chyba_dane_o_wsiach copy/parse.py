import csv
import os
import json

def UnicodeDictReader(str_data, encoding, **kwargs):
    csv_reader = csv.DictReader(str_data, **kwargs)
    # Decode the keys once
    keymap = dict((k, k.decode(encoding)) for k in csv_reader.fieldnames)
    for row in csv_reader:
        yield dict((keymap[k], v.decode(encoding)) for k, v in row.iteritems())

#dozedata = ['\xd1,\xff', '\xd2,\xfe', '3,4']
#print list(UnicodeDictReader(dozedata, 'cp1252'))



class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


tab = []



for filename in os.listdir(os.getcwd() + '/wojewodztwa'):
	with open('wojewodztwa/' + filename) as file:
		for line in file:
			split = line.split(';')
			if (len(split) >= 14 and split[1].isdigit and len(split[1]) == 7):
				#print split[0], split[1], split[2]

				datum = {}
				datum['name'] = split[0]
				datum['teryt'] = split[1]
				datum['population'] = split[2]
				tab.append(datum)



#def UnicodeDictReader(utf8_data, **kwargs):
#    csv_reader = csv.DictReader(utf8_data, **kwargs)
#    for row in csv_reader:
#        yield {key: unicode(value, 'utf-8') for key, value in row.iteritems()}
#
#
#licznik = 0
#
#with open('../miejscowosci_zsumowane_dwie.csv', 'rb') as file:
#	text = csv.DictReader(file)
#	for row in text:
#		data = {key: unicode(value, 'utf-8') for key, value in row.iteritems()}
#		print data
#		print licznik
#		licznik += 1

#print tab


print json.dumps(tab, sort_keys=True, indent=4, separators=(',', ': '))