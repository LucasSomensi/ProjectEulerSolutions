#!/usr/bin/python
import sys
from math import *

gone = {}

def ways(number):
    if number == 1 or number==0: return 1
    if not gone.has_key(number):
        if number%2 == 0:
            gone[number] = ways(number/2)+ways(number/2-1)
            return gone[number]
        gone[number] = ways((number-1)/2)
        return gone[number]
    return gone[number]

def rep(n):
    result = tuple()
    for x in [int(y) for y in list(bin(n)[2:])]:
        result = tuple([x])+result
    return result



##for x in xrange(1, 50):
##    gone = {}
##    print x, bin(x)[2:], ways(rep(x))

print ways(10**25)
