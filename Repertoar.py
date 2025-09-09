# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:55:53 2022

@author: nadja
"""

def ucitajRepertoar():
    for line in open('fajlovi/repertoar.txt','r',encoding='utf8').readlines():
        if len(line)>1:
            pr = ucitajProjekciju(line)
            projekcije.append(pr)

def ucitajProjekciju(line):
    if line[-1] == "\n":
        line = line[:-1]
    naslov, datum, vreme, cena, brojSedista, brKarata = line.split("|")
    projekcija = {
        'naslov':naslov,
        'datum':datum,
        'vreme':vreme,
        'cena':int(cena),
        'broj sedišta':int(brojSedista),
        'prodate karte':int(brKarata)
        }
    return projekcija

def upisiProjekciju(pr):
    return '|'.join([pr['naslov'], pr['datum'], pr['vreme'], str(pr['cena']), str(pr['broj sedišta']), str(pr['prodate karte'])])

def nadjiProjekciju(film, dan, sat):
    for f in projekcije:
        if f['naslov'] == film and f['datum'] == dan and f['vreme'] == sat:
            return f
    return None

def napraviProjekciju(naslov, datum, vreme):
    pr = {}
    pr['naslov'] = naslov
    pr['datum'] = datum
    pr['vreme'] = vreme
    for p in projekcije:
        if p['naslov'] == pr['naslov']:
            pr['cena'] = p['cena']
    pr['broj sedišta'] = 200
    pr['prodate karte'] = 0
    projekcije.append(pr)
    sacuvajProjekcije()

def sacuvajProjekcije():
    fajl = open('fajlovi/repertoar.txt', 'w', encoding='utf8')
    for pr in projekcije:
        fajl.write(upisiProjekciju(pr))
        fajl.write("\n")
    fajl.close()

def promeniVremeProjekcije(pr):
    noviSat = int(input("Unesite u koliko sati će se prikazivati projekcija (u 24h formatu): "))
    noviMinut = int(input('Unesite u koliko minuta će se prikazivati projekcija :'))
    if -1<noviSat<25 and -1<noviMinut<61:
        if noviSat<10 and noviMinut<10:
            noviSatS = '0' + str(noviSat)
            noviMinutS = '0' + str(noviMinut)
        elif noviSat<10:
            noviSatS = '0' + str(noviSat)
            noviMinutS = str(noviMinut)
        elif noviMinut<10:
            noviSatS = str(noviSat)
            noviMinutS = '0' + str(noviMinut)
        else:
            noviSatS = str(noviSat)
            noviMinutS = str(noviMinut)
        novoVreme = noviSatS + ':' + noviMinutS
        pr['vreme'] = novoVreme
        sacuvajProjekcije()
        print('\nUspešno uneto novo vreme projekcije!')
    else:
        print('\nNije dobro uneto vreme!')
        
def proveriSedista(sed, film):
    if sed < 1:
        print("\nMorate uzeti bar jedno mesto!")
        return 0
    elif film['broj sedišta']>=sed:
        cena = sed*film['cena']
        film['broj sedišta'] -= sed
        film['prodate karte'] += sed
        return cena
    else:
        print('\nTražili ste više sedišta nego što je ponuđeno!')
        return 0

def stampajHeader():
    print('Repertoar:')
    print(100*'-')
    print('{0:^25} {1:^19}  {2:^10} {3:^9} {4:^15} {5:^10}'.format('Naslov:','Datum:','Vreme:','Cena:','Broj sedišta:','Prodate karte:'))
    print(100*'-')

def stampajProjekciju(pr):
    return '|{0:^25}|{1:^19}|{2:^10}|{3:^9}|{4:^15}|{5:^14}|'.format(
        pr['naslov'],
        pr['datum'],
        pr['vreme'],
        pr['cena'],
        pr['broj sedišta'],
        pr['prodate karte'])

def stampajSveProjekcije():
    res = ''
    for pr in projekcije:
        res += stampajProjekciju(pr) + "\n"
    res += 100*'-'
    return res

projekcije = []
ucitajRepertoar()