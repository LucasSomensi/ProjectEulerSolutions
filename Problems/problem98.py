#!/usr/bin/python
import sys

f=open('/home/lucas/euler/files/words.txt', 'r')
palavras=eval('['+f.readline()+']')
f.close()


def letcount(n):
    count=[0]*26
    for x in n:
        count[ord(x)-65]+=1
    return count

def mask(n, st):
    n=str(n)
    if len(n)!=len(st): return False
    for x in xrange(len(n)):
        for y in xrange(len(n)):
            if n[y]==n[x] and st[y]!=st[x]: return False
    return True


def maskany(st):
    s=10**(len(st)/2)
    while s**2<=10**(len(st)+1):
        if mask(s**2, st):
            return True
        s+=1
    return False




anagrams=[]
for x in xrange(len(palavras)):
    print x
    a=letcount(palavras[x])
    for y in xrange(x):
        if letcount(palavras[y])==a:
            anagrams.append([palavras[x], palavras[y]])

print anagrams




def allmasks(st):
    s=10**((len(st)-1)/2)
    result=[]
    while s**2<=10**(len(st)+1):
        if mask(s**2, st):
            result.append(s**2)
        s+=1
    return result


def get_sub(st, n):
    n=str(n)
    sub={}
    for x in xrange(len(st)):
        sub[st[x]]=n[x]
    return sub

def do_sub(sub, st):
    result=''
    for x in st: result+=sub[x]
    return int(result)

for par in anagrams:
    for x in allmasks(par[0]):
        if do_sub(get_sub(par[0], x), par[1])**0.5%1==0: print par[0], par[1], x, do_sub(get_sub(par[0], x), par[1])
