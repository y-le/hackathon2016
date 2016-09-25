#import xml.etree.ElementTree as ET
import json

#tree = ET.parse('SIMC-3.xml')
#root = tree.getroot()

#catalog = list(root)[0]
#
#rows = catalog.findall("row")
#
#data = []
#
#for row in rows:
#	d = {x.attrib['name']:x.text for x in row.findall('col')}
#
#	datum = {}
#
#	datum['teryt'] = d['WOJ'] + d['POW'] + d['GMI']
#
#	datum['simc'] = d['SYM']
#	datum['nazwa'] = d['NAZWA']
#
#	data.append(datum)
#
#print(json.dumps(data))

from bs4 import BeautifulSoup
soup = BeautifulSoup(open('SIMC-3.xml'))

data = []

rows = soup.find_all('row')
for row in rows:
	cols = row.find_all('col')
	d = {col.attrs['name']:col.text for col in cols}
	
	datum = {}
	datum['teryt'] = d['WOJ'] + d['POW'] + d['GMI']
	datum['simc'] = d['SYM']
	datum['nazwa'] = d['NAZWA']

	data.append(datum)

	
print(json.dumps(data))

