from math import e, ceil, floor, log

def gcd(a, b):
    if a==0: return b
    return gcd(b%a,a) 

def k(N):
    k1 = floor(N/e)
    k2 = ceil(N/e)
    if  k1*log(N)+k2*log(k2) > log(N)*k2+log(k1)*k1: return k1
    return k2

def M(N):
    return (N//gcd(N,k(N)), k(N)//gcd(N,k(N)))

def teste(N):
    a = M(N)[1]
    while a%2==0: a//=2
    while a%5==0: a//=5
    return a==1

def D(N):
    if teste(N): return -N
    return N

def sumD(inicio, fim):
    return sum([D(x) for x in range(inicio, fim+1)])


print (sumD(5,10000))
