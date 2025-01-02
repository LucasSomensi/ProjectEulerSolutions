#!/usr/bin/python
import sys
import string

primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
gone={}

def squarefree(n):
    for x in primes:
        if n%x**2==0: return False
    return True


def increment(line):
    result=[1]
    for x in xrange(0, len(line)-1):
        result.append(line[x]+line[x+1])
    result.append(1)
    return result

result=0
line=[1]
for n in xrange(51):
    print n
    for x in line:
        if not gone.has_key(x):
            gone[x]=True
            if squarefree(x):
                print '  ', x
                result+=x
    line=increment(line)

print result
    
