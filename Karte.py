# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 15:56:56 2022

@author: nadja
"""

def ucitajKarte():
    for k in open("fajlovi/prodateKarte.txt", "r", encoding="utf8").readlines():
        if len(k)>1:
            karta = ucitajKartu(k)
            karte.append(karta)
   
def ucitajKartu(k):
    if k[-1] == "\n":
        k = k[:-1]
    naslov, datum, vreme, sedista, cenaKarata = k.split("|")
    karta = {
        'naslov':naslov,
        'datum':datum,
        'vreme':vreme,
        'sedišta':sedista,
        'cena karata':cenaKarata
        }
    return karta
       
def upisiKartu(karta):
    return '|'.join([karta['naslov'], karta['datum'], karta['vreme'], str(karta['sedišta']), str(karta['cena karata'])])

def dodajKartu(film, cena, sed):
    film['sedišta'] = sed
    film['cena karata'] = cena
    karte.append(film)
    sacuvajKarte()

def sacuvajKarte():
    fajl = open("fajlovi/prodateKarte.txt", "w", encoding="utf8")
    for k in karte:
        fajl.write(upisiKartu(k))
        fajl.write('\n')
    fajl.close()

def stampajHeader():
    print('Kupljene karte: ')
    print(77*'-')
    print('{0:^20} {1:^19} {2:^10} {3:^13} {4:^9} '.format('Naziv filma:','Datum:','Vreme:','Broj sedišta:','Cena:'))
    print(77*'-')

def stampajKartu(k):
    return '{0:^20} {1:^19} {2:^10} {3:^13} {4:^9}'.format(
        k['naslov'],
        k['datum'],
        k['vreme'],
        k['sedišta'],
        k['cena karata'])

def stampajKarte():
    res = ''
    for k in karte:
        res += stampajKartu(k)
        res += (77*'-') + "\n"
    return res

karte = []
ucitajKarte()