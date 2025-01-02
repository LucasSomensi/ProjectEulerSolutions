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



result=0
for x in xrange(limit+1):
    if len(continued(x))%2==0: result+=1


print result
