#!/usr/bin/python
import sys
import string



limit=10**7
divisors=[0]*(limit+1)
for x in xrange(1, limit+1):
    if x%10000==0: print x
    for y in xrange(x, limit+1, x):
        divisors[y]+=1

count=0
for n in xrange(2, 10**7):
    if divisors[n]==divisors[n+1]:
        count+=1

print count
