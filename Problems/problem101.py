#!/usr/bin/python
import sys
import random
import time




def interpolate(x, data):
    if len(data)==1: return data[0][1]
    return ((interpolate(x, data[:-1])*(x-data[-1][0])-interpolate(x, data[1:])*(x-data[0][0]))/
            float(data[0][0]-data[-1][0]))


mydata=[(n, 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10)
        for n in xrange(1, 11)]

print mydata
for x in xrange(1, len(mydata)+1):
    print interpolate(x+1, mydata[:x]), x, mydata[:x]
print sum(interpolate(x+1, mydata[:x]) for x in xrange(1, len(mydata)+1))
