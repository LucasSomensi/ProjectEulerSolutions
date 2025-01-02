#!/usr/bin/python
import sys

triangle=[(x*(x+1))/2 for x in xrange(1, 1000) if 1000<=(x*(x+1))/2<=9999]
square=[x**2 for x in xrange(1, 1000) if 1000<=x**2<=9999]
pentagonal=[(x*(3*x-1))/2 for x in xrange(1, 1000) if 1000<=(x*(3*x-1))/2<=9999]
hexagonal=[x*(2*x-1) for x in xrange(1, 1000) if 1000<=x*(2*x-1)<=9999]
heptagonal=[(x*(5*x-3))/2 for x in xrange(1, 1000) if 1000<=(x*(5*x-3))/2<=9999]
octagonal=[x*(3*x-2) for x in xrange(1, 1000) if 1000<=x*(3*x-2)<=9999]


def solve(sets, gone=[]):
    if len(sets)==0:
        return [gone]
    result=[]
    if len(gone)==0:
        for x in xrange(len(sets)):
            for y in sets[x]:
                result+=solve(sets[:x]+sets[x+1:], [y])
        return result
    for x in xrange(len(sets)):
        for y in sets[x]:
            if str(y)[:2]==str(gone[-1])[-2:]:
                result+=solve(sets[:x]+sets[x+1:], gone+[y])
    return result



print solve([triangle, square, pentagonal, hexagonal, heptagonal, octagonal])

