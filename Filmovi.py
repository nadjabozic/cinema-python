# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 14:46:31 2022

@author: nadja
"""

def ucitajFilmove():
    for line in open('fajlovi/filmovi.txt', 'r', encoding="utf8").readlines():
        if len(line)>1:
            film = ucitajFilm(line)
            filmovi.append(film)
    
def ucitajFilm(line):
    if line[-1] == "\n":
        line = line[:-1]
    naziv, zanr, reziser, glavnaUloga, trajanje, godina = line.split("|")
    film = {
        'naslov':naziv,
        'žanr':zanr,
        'režiser':reziser,
        'glavna uloga':glavnaUloga,
        'trajanje':trajanje,
        'godina':godina
        }
    return film

def traziFilm(naslov):
    for f in filmovi:
        if f['naslov'].upper() == naslov.upper():
            return f
    return None

def stampajHeader():
    print(118*'-')
    print('{0:^20} {1:^30} {2:^20} {3:^20} {4:^15} {5:^8}'.format('Naziv:','Žanr:','Režiser:','Glavna Uloga:','Trajanje:','Godina:'))
    print(118*'-')

def stampajFilm(film):
    return u'{0:^20}|{1:^30}|{2:^20}|{3:^20}|{4:^15}|{5:^6}'.format(
        film['naslov'],
        film['žanr'],
        film['režiser'],
        film['glavna uloga'],
        film['trajanje'],
        film['godina'])
    
def stampajSveFilmove():
    rez = ''
    for film in filmovi:
        rez += stampajFilm(film) + '\n'
    return rez

filmovi = []
ucitajFilmove()