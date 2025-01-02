#!/usr/bin/python
import sys
import string

limit=10**8
sieve=[False, False]+[True]*limit
for x in xrange(2, limit):
    if x%100000==0: print x
    if sieve[x]==True:
        for y in xrange(2*x, limit, x):
            sieve[y]=False

primes = [x for x in xrange(2, limit) if sieve[x]==True]
pi=len(primes)
del(sieve)


print 'comecando a multiplicar'
result=0
x=0
while x<pi:
    if x%1000==0:
        print x, result
    y=0
    while y<=x and primes[x]*primes[y]<limit:
        result+=1
        y+=1
    x+=1


print result
