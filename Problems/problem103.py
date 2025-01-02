import sys
from math import *



def quicksort(lista):
    if len(lista)==0 or len(lista)==1: return lista
    return quicksort([x for x in lista if x<lista[0]])+\
           [x for x in lista if x==lista[0]]+\
           quicksort([x for x in lista if x>lista[0]])



def disjuntos(lista1, lista2):
    for x in lista1:
        if x in lista2: return False
    return True

def subsets(lista):
    result = [[]]
    for x in range(len(lista)):
        result+=[[lista[x]]+y for y in subsets(lista[x+1:])]
    return result


def subset_pairs(lista):
    subs = subsets(lista)
    result = []
    for x in range(1, len(subs)):
        for y in subs[x+1:]:
            if disjuntos(subs[x], y): result.append([subs[x],y])
    return result


    
def teste1(lista):
    lista = quicksort(lista)
    for x in range(len(lista)-1):
        if lista[x]==lista[x+1]: return False
    pairs = subset_pairs(lista)
    for x in pairs:
        if sum(x[0])==sum(x[1]) and len(x[0])==len(x[1]):
            return False
    return True
    

def teste2(lista):
    lista = quicksort(lista)
    for x in range(2, ceil(len(lista)/2)+1):
        if sum(lista[:x])<=sum(lista[-x+1:]): return False
    return True

def teste(lista):
    if teste2(lista) and teste1(lista): return True

print (teste([20, 31, 38, 39, 40, 42, 45]))
memo = float('infinity')

for a in range(-3, 3):
    for b in range(-3, 3):
        print(b)
        for c in range(-3, 3):
            for d in range(c-1, 3):
                for e in range(d-1, 3):
                    for f in range(e-2, 3):
                        for g in range(f-3, 3):
                            if teste([20+a, 31+b, 38+c, 39+d, 40+e, 42+f, 45+g]) and sum([20+a, 31+b, 38+c, 39+d, 40+e, 42+f, 45+g])<memo:
                                memo = sum([20+a, 31+b, 38+c, 39+d, 40+e, 42+f, 45+g])
                                print([20+a, 31+b, 38+c, 39+d, 40+e, 42+f, 45+g])
                            
                        
        
