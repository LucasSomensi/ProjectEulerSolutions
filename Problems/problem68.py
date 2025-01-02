#!/usr/bin/python
import sys

def perms(lista):
    if len(lista)==1: return [lista]
    result=[]
    for x in xrange(len(lista)):
        result+=[[lista[x]]+y for y in perms(lista[:x]+lista[x+1:])]
    return result

def arms(x):
    return [(x[0], x[1], x[2]), (x[3],x[2],x[4]), (x[5], x[4], x[6]),
            (x[7], x[6], x[8]), (x[9], x[8], x[1])]


def test(solucao):
    a=arms(solucao)
    valor=sum(a[0])
    for x in a:
        if sum(x)!=valor: return False
    return True


def sort(x):
    for y in xrange(len(x)):
        if x[y][0]==min([x[z][0] for z in xrange(len(x))]):
            return x[y:]+x[:y]


def string(solucao):
    a=sort(arms(solucao))
    result=''
    for x in a:
        for y in x:
            result+=str(y)
    return result
        
    
    


solucoes=[int(y) for y in list(set([string(x) for x in perms([1,2,3,4,5,6,7,8,9,10]) if test(x)]))]
solucoes.sort()
print solucoes
