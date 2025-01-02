#!/usr/bin/python
import sys
import string

def divides(n):
    a=1
    b=1
    c=1
    gone={(1,1,1): True}
    a, b, c = b, c, (a+b+c)%n
    while not gone.has_key((a,b,c)):
        if c==0: return True
        gone[(a,b,c)]=True
        a, b, c = b, c, (a+b+c)%n
    return False


goal=124

n=27
result=[]
while len(result)!=goal:
    print n, len(result)
    if not divides(n): result.append(n)
    n+=2

print result[-1]
