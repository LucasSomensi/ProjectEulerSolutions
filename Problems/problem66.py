#!/usr/bin/python
import sys
import time
from math import *


limit=1000



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


def pell(s):
    if sqrt(s)%1==0: return (1,0)
    a=continued(s)
    period=len(a)-1
    r=period-1
    if r%2==0: a+=a[1:-1]
    else: a=a[:-1]
    n=1
    d=0
    while len(a)!=0:
        n, d = d, n
        n+=d*a[-1]
        del(a[-1])
    return (n, d)



best=1
for x in xrange(1, limit+1):
    if pell(x)[0]>=pell(best)[0]: best=x
    print x, best

print best, pell(best)
