#!/usr/bin/python
import sys

goal=7
familias={}

def subsets(lista):
    if len(lista)==0: return [[]]
    if len(lista)==1: return [[], lista]
    result=[[]]
    for x in range(len(lista)):
        result+=[lista[x:x+1]+y for y in subsets(lista[:x])]
    return result


def myreplace(st, pos):
    result=''
    for x in xrange(len(st)):
        if x not in pos: result+=st[x]
        else: result+='_'
    return result

def families(n):
    n=str(n)
    result=[]
    for x in xrange(0, 10):
        if not str(x) in n: continue
        pos=[]
        for y in xrange(0, len(n)):
            if n[y]==str(x): pos.append(y)
        for y in subsets(pos):
            if y==[]: continue
            result.append(myreplace(n, y))
    return result


def prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n%3==0: return False
    i=6
    while (i-1)**2<=n:
        if n%(i-1)==0: return False
        if n%(i+1)==0: return False
        i+=6
    return True

n=11
while True:
    if prime(n):
        for x in families(n):
            if familias.has_key(x):
                familias[x].append(n)
                if len(familias[x])>=goal: print familias[x]; #exit()
            else:
                familias[x]=[n]
    n+=2
