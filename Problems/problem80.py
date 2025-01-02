#!/usr/bin/python
import sys
import time
from math import *


limit=10000


def continued(s):
    if sqrt(s)%1==0: return [s]
    a=[int(sqrt(s))]
    m=[0]
    d=[1]
    while a[-1]!=a[0]*2:
        m.append(a[-1]*d[-1]-m[-1])
        d.append((s-m[-1]**2)/d[-1])
        a.append((a[0]+m[-1])/d[-1])
    return a


def approx(s, level=1):
    a=continued(s)
    period=len(a)-1
    for x in xrange(level-1):
        a+=a[1:period+1]
    n=1
    d=0
    while len(a)!=0:
        n, d = d, n
        n+=d*a[-1]
        del(a[-1])
    return (n, d)


def mysum(x):
    if sqrt(x)%1==0: return 0
    a=str((approx(x, 1000)[0]*10**99)/approx(x, 1000)[1])
    print x, len(a)
    return sum(int(i) for i in a)
    


print sum(mysum(x) for x in xrange(1, 100))
    
