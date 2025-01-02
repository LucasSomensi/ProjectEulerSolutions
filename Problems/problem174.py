#!/usr/bin/python
import sys
from math import log

limit=10**6

solutions=[0]*(limit+1)

hole=1
while (hole+2)**2-hole**2<=limit:
    if hole%1000==0: print hole
    border=hole+2
    while border**2-hole**2<=limit:
        solutions[border**2-hole**2]+=1
        border+=2
    hole+=1

print len(filter(lambda x: x in range(1, 11), solutions))
