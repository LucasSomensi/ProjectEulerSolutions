#!/usr/bin/python
import sys

limit=int(sys.argv[1])

def gcd(a, b):
    if b==0: return a
    return gcd(b, a%b)


def A(n):
    remainder=10%(9*n)
    print n
    i=1
    while remainder!=1:
        i+=1
        remainder=(remainder*10)%(9*n)
    if i>=1000000: print n, i; exit
    return i


def prime(n):
    if n%2==0: return False
    if n%3==0: return False
    i=6
    while (i-1)**2<=n:
        if n%(i-1)==0: return False
        if n%(i+1)==0: return False
        i+=6
    return True

a=[x for x in xrange(4, limit) if gcd(x, 10)==1 and (x-1)%A(x)==0
       and not prime(x)]

print a
print len(a)
print sum(a[:25])
