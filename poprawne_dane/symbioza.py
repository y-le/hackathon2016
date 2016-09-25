
import json
ludnosc = json.load(open('LUDNOSC.json', newline='', encoding='utf-8'))
# TERYT z dokladnoscia do 4 pierwszych cyfr
''' {"teryt": "180100", "simc": "1801032", "nazwa": "gm.w. Czarna", "populacja": "2421"} '''

lacznik = json.load(open('LACZNIK.json', newline='', encoding='utf-8'))
''' {"simc": "0454741", "nazwa": "Andrzej\u00f3wka", "teryt": "121011"} '''

wspolrzedne = json.load(open('WSPOLRZEDNE.json', newline='', encoding='utf-16'))
''' {
        "d\u0142ugo\u015b\u0107 geograficzna": "19.23055555555555555555555556",
        "identyfikator jednostki podzia\u0142u terytorialnego kraju": "2475011",
        "nazwa g\u0142\u00f3wna": "Osiedle Kowalczyka",
        "szeroko\u015b\u0107 geograficzna": "50.27027777777777777777777778"
    }
 '''

def ludnosc_key(row):
    return (row['teryt'], row['simc'])

def wspolrzedne_key(row):
    return (row["identyfikator jednostki podzia\u0142u terytorialnego kraju"], row["nazwa g\u0142\u00f3wna"])



subres = []
import editdistance

def join1():
    for x in lacznik:
        x_teryt, x_simc = x['teryt'], x['simc']
            for p in ludnosc:
                p_teryt, p_simc = ludnosc_key(p)
                if x_teryt == p_teryt[:4] and x_simc == p_simc:
                    # SIMC jest pewnikiem
                    r = p.clone()
                    r.update(x)
                    yield r

def join2():
    for x in join1():
        x_teryt, x_name = x['teryt'], x['name']
            for q in wspolrzedne:
                q_teryt, q_name = wspolrzedne_key(q)
                if editdistance.eval(x_name, q_name.lower()) <= 3:
                    r = q.clone()
                    r.update(x)
                    yield r

open('BAZA.json', 'w', encoding='utf-8').write(json.dumps(list(join2())))
