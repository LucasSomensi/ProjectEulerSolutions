#!/usr/bin/python
import sys

#easiest problem ever

def solve(a):
    n=1
    gone={}
    term=[a+1, a-1]
    r=(term[0]+term[1])%a**2
    best=r
    gone[tuple(term)]=True
    term[0]=(term[0]*(a+1))%a**2
    term[1]=(term[1]*(a-1))%a**2
    while not gone.has_key(tuple(term)):
        best=max(best, (term[0]+term[1])%a**2)
        term[0]=(term[0]*(a+1))%a**2
        term[1]=(term[1]*(a-1))%a**2
    return best

print sum(solve(x) for x in xrange(3, 1001))
        
