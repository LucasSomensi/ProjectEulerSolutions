#!/usr/bin/python
import sys

limit=2000000


def A(n):
    remainder=10%(9*n)
    print n
    i=1
    while remainder!=1:
        i+=1
        remainder=(remainder*10)%(9*n)
    if i>=1000000: print n, i; exit
    return i

[A(x) for x in xrange(1000000, limit) if x%2!=0 and x%5!=0]
