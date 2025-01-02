#!/usr/bin/python
import sys


limit=int(sys.argv[1])
chain_len=int(sys.argv[2])


phis=range(0, limit)
for n in xrange(2, limit):
    if n%10000==0: print n
    if phis[n]==n:
        for m in xrange(n,limit,n):
            phis[m]-=phis[m]/n

print 'tabela feita'


def chain(start):
    count=2
    current=phis[start]
    while current!=1:
        current=phis[current]
        count+=1
    return count

result=0
for x in xrange(2, limit):
    if x%10000==0: print x
    if phis[x]==x-1 and chain(x)==chain_len:
        result+=x

print result
