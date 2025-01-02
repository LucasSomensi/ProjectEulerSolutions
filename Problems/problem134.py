#!/usr/bin/python
import sys
from math import *


def extend(a,b):
    if b==0: return (1,0,a)
    temp=extend(b, a%b)
    return (temp[1], temp[0]-(a//b)*temp[1], temp[2])

def reverse(p, d): return (extend(p, d)[0])%d
def dig(a): return 10**int(ceil(log10(a+1)))
def R(p1, p2): return p2*(p1*reverse(p2, dig(p1))%dig(p1))



seive = [False, False]+[True]*(1000004-1)
for x in xrange(2, len(seive)//2+1):
    if seive[x]==True:
        for y in xrange(2*x, len(seive), x):
            seive[y]=False
primes = [x for x in xrange(len(seive)) if seive[x]==True]
print 'completo'

result = 0
for x in xrange(len(primes)):
    if 5 <= primes[x] <= 1000000:
        result += R(primes[x], primes[x+1])
        print primes[x], primes[x+1], R(primes[x], primes[x+1])

print result
