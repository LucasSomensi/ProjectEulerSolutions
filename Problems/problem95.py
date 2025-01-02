#!/usr/bin/python
import sys


#codigo lindo abaixo

limit=1000000

sums=[0]*(limit+1)
for n in xrange(1, limit+1):
    if n%1000==0: print n
    for m in xrange(2*n, limit+1, n):
        sums[m]+=n

print 'tabela calculada'


def chain(start):
    visited={start:True}
    current=sums[start]
    count=1
    while current!=start:
        if current<=1: return 0
        if current>limit: return 0
        if current<start: return 0
        if visited.has_key(current): return 0
        visited[current]=True
        current=sums[current]
        count+=1
    return count
    

longest=1
smaller=0
for x in xrange(2, limit+1):
    if x%1000==0: print x
    a=chain(x)
    if a>longest:
        longest=a
        smaller=x

print smaller
