from math import *

A = '1415926535'
B = '8979323846'

A='1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
B='8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196'

def F(n):
    a=1
    b=1
    for x in range(2, n):
        a, b = b, a+b
    return b

def F_1(n):
    k = 2
    while F(k)<n: k+=1
    return k

def d(n, pos):
    #print ('   ', n, pos)
    if n==1:
        return A[pos-1]
    if n==2:
        return B[pos-1]
    if pos>len(A)*F(n-2): return d(n-1, pos-len(A)*F(n-2))
    else: return d(n-2, pos)

def D(pos):
    return int(d(F_1(ceil(pos/len(A))), pos))


print (sum([D((127+19*n)*7**n)*10**n for n in range(0, 18)]))
