#!/usr/bin/python
import sys
import time


def subsets(lista):
    result=[[]]
    for index, x in enumerate(lista):
        result+=[[x]+y for y in subsets(lista[index+1:])]
    return result

def ntsubsets(lista):
    result=subsets(lista)
    return [x for x in result if len(x)!=len(lista) and len(x)!=0]


def inverso(conjunto1, conjunto2):
    return [x for x in conjunto1 if x not in conjunto2]

def combine(numeros):
    if len(numeros)<=1: return numeros
    result=[]
    result+=[x/y for sub in ntsubsets(numeros) for x in combine(sub) for y in combine(inverso(numeros, sub))
             if y!=0 and x%y==0]
    result+=[y*x for sub in ntsubsets(numeros) for x in combine(sub) for y in combine(inverso(numeros, sub))]
    result+=[y+x for sub in ntsubsets(numeros) for x in combine(sub) for y in combine(inverso(numeros, sub))]
    result+=[y-x for sub in ntsubsets(numeros) for x in combine(sub) for y in combine(inverso(numeros, sub))]
    return list(set(result))

def first_missing(lista):
    n=1
    while n in lista:
        n+=1
    return n






best=1
result=[]
for d in range(4, 10):
    print d
    for c in range(3, d):
        for b in range(2, c):
            for a in range(1, b):
                if first_missing(combine([a,b,c,d]))>=best:
                    result=[a,b,c,d]
                    best=first_missing(combine([a,b,c,d]))
                    print best
                    print combine([a,b,c,d])
print result
