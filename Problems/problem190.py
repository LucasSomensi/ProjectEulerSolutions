import sys
from decimal import *
from math import *

def product(lista):
    result=1
    for x in lista:
        result*=x
    return result

def P(lista):
    return product([lista[x]**(x+1) for x in range(len(lista))])*(len(lista)+1-sum(lista))**(len(lista)+1)

def better(lista, precision=0.1):
    result = lista[:]
    for x in range(len(lista)):
        if P(lista[:x]+[lista[x]+precision]+lista[x+1:])>P(lista):
            result[x]=lista[x]+precision
        elif P(lista[:x]+[lista[x]-precision]+lista[x+1:])>P(lista):
            result[x]=lista[x]-precision
    return result

def Pm(m):
    print(m)
    current = [1]*(m-1)
    for precision in [1/10**x for x in range(1, 7)]:
        for x in range(1, 100): current=better(current, precision)
    return P(current)

print(sum(floor(Pm(x)) for x  in range(2,16)))

