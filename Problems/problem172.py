#!/usr/bin/python
import sys


solved={}
p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def ways(n, gone=1):
    if n==0: return 1
    if not solved.has_key((n, gone)):
        result=0
        if gone==1:
            for x in xrange(1, 10):
                result+=ways(n-1, p[x])
        else:
            for x in xrange(0, 10):
                if gone%p[x]**3!=0:
                    result+=ways(n-1, gone*p[x])
        solved[(n, gone)]=result
    return solved[(n, gone)]

a=int(sys.argv[1])

print ways(a)
print len(str(ways(a)))
    
