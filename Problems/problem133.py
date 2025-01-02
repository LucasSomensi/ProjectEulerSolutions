#!/usr/bin/python
import sys



limit=100000
sieve=[True]*limit
for x in xrange(2,limit):
    if sieve[x]==True:
        for y in xrange(2*x, limit, x):
            sieve[y]=False
primes=[x for x in xrange(2, limit) if sieve[x]]
del(sieve)


gone={}



def modexp(a, b, n):
    if b<=2: return (a**b)%n
    if b%2==0: return (modexp(a, b/2, n)**2)%n
    else: return (a*(modexp(a, b//2, n)**2)%n)%n

def div(k, n):
    return modexp(10, k, 9*n)==1


def check(n):
    while n%10==0:
        n/=10
    while n%5==0:
        n/=5
    while n%2==0:
        n/=2
    return n==1


def factor(k):
    for x in primes:
        if not gone.has_key(x):
            if div(k,x):
                gone[x]=True


for x in xrange(2, limit):
    if check(x):
        print x
        factor(x)
result=[x for x in primes if not gone.has_key(x)]
print sum(result)
