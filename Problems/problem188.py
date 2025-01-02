#!/usr/bin/python
import sys

phi={100000000: 40000000,
     40000000: 16000000,
     16000000: 6400000,
     6400000: 25600000,
     25600000: 10240000,
     10240000: 4096000,
     4096000: 1638400,
     1638400: 655360,
     655360: 262144}

def modhexp(lista, n, depth=0):
    print depth, n
    if n==1: return 0
    if len(lista)==1: return lista[0]
    if phi.has_key(n): new_n=phi[n]
    else: new_n=n/2
    try:
        return pow(lista[0], modhexp(lista[1:], new_n, depth+1), n)
    except:
        exit()

print modhexp([1777]*1855, 10**8)
