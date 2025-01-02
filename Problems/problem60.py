#!/usr/bin/python
import sys


primos=[2,3,5,7]
solved={}




def prime(n):
    if not solved.has_key(n):
        if n==2 or n==3: solved[n]=True; return True
        if n%2==0 or n%3==0: solved[n]=False; return False
        i=6
        while (i-1)**2<=n:
            if n%(i-1)==0: solved[n]=False; return False
            if n%(i+1)==0: solved[n]=False; return False
            i+=6
        solved[n]=True
        return True
    return solved[n]


def concat(a, b):
    return prime(int(str(b)+str(a))) and prime(int(str(a)+str(b)))



def addone():
    n=primos[-1]
    while True:
        n+=1
        if prime(n):
            primos.append(n)
            return
        
        



while True:
    addone()
    a=primos[-1]
    print a
    for b in primos[:-1]:
        if not (concat(a,b)):continue
        for c in primos[:-2]:
            if not (concat(a,c) and concat(b,c)):continue
            for d in primos[:-3]:
                if not (concat(a,d) and concat(b,d) and concat(c,d)): continue
                for e in primos[:-4]:
                    if not (concat(a,e) and concat(b,e) and concat(c,e) and concat(d,e)): continue
                    print a,b,c,d, e, sum([a,b,c,d,e])
                    exit()
