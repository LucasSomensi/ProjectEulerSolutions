#!/usr/bin/python
import sys


solved={}


def ways(n, last='  ', limit=9):
    if n==0: return 1
    if not solved.has_key((n, limit, last)):
        result=0
        if last=='  ':
            for x in xrange(1, 10):
                result+=ways(n-1, ' '+str(x))
        elif last[0]==' ':
            for x in xrange(0, 10):
                result+=ways(n-1, last[1]+str(x))
        else:
            for x in xrange(0, 10):
                if int(last[0])+int(last[1])+x<=limit:
                    result+=ways(n-1, last[1]+str(x))
        solved[(n, limit, last)]=result
    return solved[(n, limit, last)]

print ways(20)
print len(str(ways(20)))
    
