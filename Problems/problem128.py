#!/usr/bin/python
import sys
from math import *

def first(a):
    if a==0: return 1
    return 2+(6*(a-1)*a)/2

def n(line, pos):
    if line==0: mod = 1
    else: mod = 6*line
    return first(line)+(pos%mod)

def last(line):
    if line == 0: return 1
    return n(line, line*6-1)

def gps(a):
    if a==1: return (0,0)
    t = 2*int((a-2)/6)
    temp = sqrt(1 + 4*t)
    line = int((1+temp)/2)
    pos = a-first(line)
    return (line, pos)
    
    

def neigh(line, pos):
    if line==0 and pos==0: return [2,3,4,5,6,7]
    if pos%line==0:
        return [n(line, pos+1), n(line, pos-1), n(line-1, (pos*(line-1))/line), n(line+1, (pos*(line+1))/line),
                n(line+1, (pos*(line+1))/line)+1, n(line+1, (pos*(line+1))/line-1)]
    else:
        check = int(pos/line)
        rem = pos%line
        return [n(line, pos-1), n(line, pos+1), n(line-1, check*(line-1)+rem-1), n(line-1, check*(line-1)+rem),
                n(line+1, check*(line+1)+rem+1), n(line+1, check*(line+1)+rem)]

def dif(a):
    result = []
    for x in neigh(gps(a)[0], gps(a)[1]):
        result.append(abs(x-a))
    return result


memo = {}

def prime(a):
    if a==1: return False
    if a in [2, 3]: return True
    if memo.has_key(a): return memo[a]
    if a%2==0:
        memo[a]=False
        return False
    if a%3==0:
        memo[a]=False
        return False
    i=6
    while (i-1)**2<=a:
        if a%(i-1)==0:
            memo[a]=False
            return False
        if a%(i+1)==0:
            memo[a]=False
            return False
        i+=6
    memo[a]=True
    return True

def PD(a):
    result = 0
    for x in dif(a):
        if prime(x): result+=1
    return result


count = 1
for x in xrange(1, 2000000):
    if PD(n(x,0))==3:
        count+=1
        print count, n(x, 0)
    if PD(n(x, -1))==3:
        count+=1
        print count, n(x, -1)
