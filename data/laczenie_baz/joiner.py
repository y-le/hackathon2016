
p1 = open('temp_out.txt', 'rb').read().decode('utf-8')
'''
    {
        "lat": 53.58694444444445,
        "lng": 21.359444444444446,
        "name2": "Jesionowiec",
        "teryt": "2817072"
    },
'''

p2 = open('output1.txt', 'rb').read().decode('utf-8')
'''
    {
        "name": "gm. m. Boles\u0142awiec",
        "population": "40209",
        "teryt": "0201011"
    },
'''

import json
p1 = json.loads(p1)
p2 = json.loads(p2)

d = {}
for x in p1:
  d[x['name2']] = x

for x in p2:
  if x['name'] in d:
    d[x['name']]['population'] = x['population']

from pprint import pprint
#pprint(d)

open('3tys_wiosek.json', 'wb').write(json.dumps(d).encode('utf-8'))

