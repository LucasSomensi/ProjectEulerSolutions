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

i=0
for x in subset_pairs([int(x) for x in sys.argv[1:]]):
    if len(x[0])==len(x[1]):
        for k in range(len(x[1])):
            if x[0][k]>=x[1][k]:
                i+=1
                print (x[0], x[1], i)
                break
        
