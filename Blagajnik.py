# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 17:20:20 2022

@author: nadja
"""

def login(username, password):
    for blg in blagajnici:
        if blg['username'] == username and blg['password'] == password:
            return True
    return False

def ucBlagajnike():
    fajl = open('fajlovi/blagajnik.txt', 'r', encoding="utf8")
    for line in fajl.readlines():
        if len(line)>1:
            blg = ucitajBlagajnika(line)
            blagajnici.append(blg)
                      
def ucitajBlagajnika(line):
    if line[-1] == "\n":
        line = line[:-1]
    ime, prezime, username, password = line.split("|")
    blg = {
        'ime':ime,
        'prezime':prezime,
        'username':username,
        'password':password
        }
    return blg

"""
def upisiBlagajnika(blg):
    return '|'.join([blg['ime'], blg['prezime'], blg['username'], blg['password']])
"""

blagajnici = []      
ucBlagajnike()
        