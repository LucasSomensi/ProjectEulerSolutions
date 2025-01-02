#!/usr/bin/python
import sys


def modexp(a, b, n):
    if b<=2: return (a**b)%n
    if b%2==0: return (modexp(a, b/2, n)**2)%n
    else: return (a*(modexp(a, b//2, n)**2)%n)%n



def check(k, n):
    return modexp(10, k, 9*n)==1

def prime(n, lista):
    for x in lista:
        if n%x==0: return False
    return True


def factor(k, l):
    result=[]
    if check(k, 2): result.append(2)
    if check(k, 3): result.append(2)
    i=6
    while len(result)<l:
        if check(k, i-1) and prime(i-1, result): result.append(i-1); print i-1
        if check(k, i+1) and prime(i+1, result): result.append(i+1); print i+1
        i+=6
    return result


print sum(factor(1000000000, 40))
