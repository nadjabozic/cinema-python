# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 17:14:26 2022

@author: nadja
"""

import Blagajnik
import Filmovi
import Repertoar
import Karte
import matplotlib.pyplot as plt

def main():
    print('Izaberite jedno od ponuđenog: ')
    print('1. Blagajnik')
    print('2. Kupac')
    unos = input('>>> ')
    if unos == '1':
        main1()
    elif unos == '2':
        main2()
    else:
        print('Pogrešan unos!')
        return
    
"""
def main():
    print('BIOSKOP')
    if not login():
        print("Nisu unete ispravne informacije!")
        return
    unos = '0'
    while unos != 'x':
        unos = menu1()
        if unos == '1':
            stampajFilmove()
        elif unos == '2':
            stampajRepertoar()
        elif unos == '3':
            pretrazivanjeFilm()
        elif unos == '4':
            unosNoveProjekcije()
        elif unos == '5':
            promenaProjekcije()
        elif unos == '6':
            kupiKartu()
        elif unos == '7':
            kupljeneKarte()
    print('\nHvala na korišćenju naših usluga!')
"""

def main1():
    print('BIOSKOP')
    if not login():
        print("Nisu unete ispravne informacije!")
        return
    unos = '0'
    while unos != 'x':
        unos = menu1()
        if unos == '1':
            stampajFilmove()
        elif unos == '2':
            stampajRepertoar()
        elif unos == '3':
            unosNoveProjekcije()
        elif unos == '4':
            promenaProjekcije()
        elif unos == '5':
            kupljeneKarte()
    print('\nHvala na korišćenju naših usluga!')

def main2():
    print('BIOSKOP')
    unos = '0'
    while unos != 'x':
        unos = menu2()
        if unos == '1':
            stampajFilmove()
        elif unos == '2':
            stampajRepertoar()
        elif unos == '3':
            pretrazivanjeFilm()
        elif unos == '4':
            kupiKartu()
    print('\nHvala na korišćenju naših usluga!')
    
"""
def menu():
    printMenu()
    unos = input('>> ')
    while unos.lower() not in ('1', '2', '3', '4', '5', '6', '7', 'x'):
        print('Uneta opcija ne postoji!')
        printMenu()
        unos = input('>> ')
    return unos.lower()
"""

def menu1():
    printMenu1()
    unos = input('>> ')
    while unos.lower() not in ('1', '2', '3', '4', '5', 'x'):
        print('Uneta opcija ne postoji!')
        printMenu1()
        unos = input('>> ')
    return unos.lower()

def menu2():
    printMenu2()
    unos = input('>> ')
    while unos.lower() not in ('1', '2', '3', '4', 'x'):
        print('Uneta opcija ne postoji!')
        printMenu2()
        unos = input('>> ')
    return unos.lower()

"""
def printMenu():
    print()
    print('Izaberite opciju:')
    print('1. Pregled filmova')
    print('2. Repertoar')
    print('3. Pretraživanje filmova po naslovu')
    print('4. Dodavanje nove projekcije')
    print('5. Promena vremena projekcije')
    print('6. Kupovina karata')
    print('7. Prodate karte')
    print('x - izlaz')
"""
    
def printMenu1():
    print()
    print('Izaberite opciju:')
    print('1. Pregled filmova')
    print('2. Repertoar')
    print('3. Dodavanje nove projekcije')
    print('4. Promena vremena projekcije')
    print('5. Prodate karte')
    print('x - izlaz')
    
def printMenu2():
    print()
    print('Izaberite opciju:')
    print('1. Pregled filmova')
    print('2. Repertoar')
    print('3. Pretraživanje filmova po naslovu')
    print('4. Kupovina karata')
    print('x - izlaz')
    
def login():
    username = input("Unesite korisničko ime: ")
    password = input('Unesite lozinku: ')
    return Blagajnik.login(username, password)

def stampajFilmove():
    print("Pregled filmova:")
    Filmovi.stampajHeader()
    print(Filmovi.stampajSveFilmove())
    
def stampajRepertoar():
    Repertoar.stampajHeader()
    print(Repertoar.stampajSveProjekcije())
    
def pretrazivanjeFilm():
    print("Pretraživanje filmova po naslovu")
    f = input('Unesite film koji tražite: ')
    film = Filmovi.traziFilm(f)
    if film == None:
        print('\nTraženi film se ne prikazuje u bioskopu!')
    else:
        Filmovi.stampajHeader()
        print(Filmovi.stampajFilm(film))
        
def unosProjekcije():
    film = input('Unesite naslov filma: ')
    dan = input('Unesite datum projekcije: ')
    sat = input('Unesite vreme projekcije: ')
    pr = Repertoar.nadjiProjekciju(film, dan, sat)
    return pr

def unosNoveProjekcije():
    print('Unos nove projekcije')
    naslov = input('Unesite naslov filma: ')
    film = Filmovi.traziFilm(naslov)
    if film == None:
        print('\nTraženi film se ne prikazuje u bioskopu!')
    else:
        datum = input('Unesite datum nove projekcije: ')
        vreme = input('Unesite u koliko sati se prikazuje nova projekcija: ')
        pr = Repertoar.nadjiProjekciju(naslov, datum, vreme)
        if pr == None:
            Repertoar.napraviProjekciju(naslov, datum, vreme)
            print('\nUspešno dodata nova projekcija!')
            return
        print('\nUneta projekcija već postoji!')   

def promenaProjekcije():
    print('Promena vremena projekcije')
    pr = unosProjekcije()
    if pr == None:
        print('Nije dobro uneta projekcija!')
    else:
        Repertoar.promeniVremeProjekcije(pr)
    
def kupiKartu():
    print('Kupovina karata')
    pr = unosProjekcije()
    if pr == None:
        print('Greška kod traženja projekcije! Proverite da li ste uneli ispravne informacije!')
        return
    print('\nUspešno uneta projekcija!')
    sed = int(input('Unesite koliko sedišta želite: '))
    cena = Repertoar.proveriSedista(sed, pr)
    if cena == 0:
        print('\nNije uspešno kupljena karta!')
        return
    Karte.dodajKartu(pr, cena, sed)
    Repertoar.sacuvajProjekcije()
    print("\nUspešno kupljena karta po ceni", cena, "!")
    
def kupljeneKarte():
    Karte.stampajHeader()
    print(Karte.stampajKarte())
    grafikFilmovi()

def grafikFilmovi():
    ax = plt.subplot()
    ax.set_title("Broj prodatih karata po filmu")
    x_podaci = []
    y_podaci = []
    for p in Repertoar.projekcije:
        x_podaci.append(p['naslov'])
        y_podaci.append(p['prodate karte'])
    plt.bar(x_podaci, y_podaci)
    plt.xlabel('filmovi')
    plt.xticks(rotation=90)
    plt.ylabel('prodate karte')
    plt.ylim(ymin=0, ymax=200)
    plt.show()



if __name__ == '__main__':
    main()