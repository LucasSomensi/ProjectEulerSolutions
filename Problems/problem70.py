#!/usr/bin/python
import sys

def letcount(n):
    count=[0]*26
    for x in n:
        count[ord(x)-65]+=1
    return count

phis=[0,1]+range(2,10000000)

for n in xrange(2,10000000):
    if n%1000==0: print n
    if phis[n]==n:
        for m in xrange(n, 10000000, n):
            phis[m]-=phis[m]/n


smaller_ratio=5
for n in xrange(2, 10000000):
    if n%10000==0: print n
    if letcount(str(n))==letcount(str(phis[n])) and float(n)/phis[n]<smaller_ratio:
        smaller=n
        smaller_ratio=float(n)/phis[n]


print smaller, phis[smaller]
