from math import factorial
from decimal import *
import sys

def pick(k,n):#pick k from n
    return factorial(n)//(factorial(k)*factorial(n-k))

def P(f, n=1000, m0=1, target=1000000000):
    paths = 0
    for w in range(0, n+1):
        if (1+2*f)**w*(1-f)**(n-w)*m0>=1000000000:
            paths+=pick(w, n)
    return Decimal(paths)/(2**n)

print (P(float(sys.argv[1])))
