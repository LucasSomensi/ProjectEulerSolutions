#!/usr/bin/python
import sys
import time
from math import *


limit=1000


x=[15]
y=[21]

for _ in xrange(120):
    x.append(3*x[-1]+2*y[-1]-2)
    y.append(4*x[-2]+3*y[-1]-3)



print x[y.index([i for i in y if i>10**12][0])]
