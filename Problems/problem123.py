#!/usr/bin/python
import sys

def modexp(a, b, n):
    if b<=2: return (a**b)%n
    if b%2==0: return (modexp(a, b/2, n)**2)%n
    else: return (a*(modexp(a, b//2, n)**2)%n)%n



def remainder(pn, n):
    return (modexp(pn+1, n, pn**2)+modexp(pn-1, n, pn**2))%pn**2




def increment(lista):

    def test(n, lista):
        for x in lista:
            if n%x==0: return False
        return True

    n=lista[-1]+1
    while True:
        if test(n, lista):
            lista.append(n)
            return
        n+=1
        

goal=10**10

primes=[2]
n=1
while remainder(primes[-1], n)<goal:
    if n%10==0: print n
    increment(primes)
    n+=1

print n
