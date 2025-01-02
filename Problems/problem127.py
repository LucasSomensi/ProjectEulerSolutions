#!/usr/bin/python
import sys
import time

limit=int(sys.argv[1])
primes=[]
facts=[[], []]
for _ in xrange(2, limit):
    facts.append([])
for x in xrange(2, limit):
    if facts[x]==[]:
        primes.append(x)
        for y in xrange(x, limit, x):
            facts[y]+=[x]
factors={1:[]}
for x in xrange(2, limit):
    factors[x]=facts[x]
del(facts)
print 'tabela feita'
#print factors


def test(a, b, c):
    fa, fb, fc = factors[a], factors[b], factors[c]
    for x in fa:
        if x in fb or x in fc: return False
    for x in fb:
        if x in fc: return False
    return True

def rad(fatores):
    result=1
    for x in fatores:
        result*=x
    return result


#def narrow
    



t=time.time()
count=0
for c in xrange(3, limit):
    if c%1000==0: print c
    mult=1
    first=0
    second=0
    for x in primes:
        if first==0 and x not in factors[c]:
            first=x
            continue
        if x not in factors[c]:
            second=x
            break
    if rad(factors[c])*first*second>=c:
        if test(c, c-1, 1) and rad(factors[c]+factors[c-1])<c:
            count+=c
        continue
    for b in xrange(1, (c+1)//2):
        if not test(c, b, c-b):
            continue
        if rad(factors[c-b]+factors[b]+factors[c])<c:
            count+=c


print count
print time.time()-t 

