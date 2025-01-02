from math import *

memo = {}

def anagram(n, repetidos):
    result = factorial(n)
    for x in repetidos: result//=factorial(x)
    return result

def divide(n, maximo, k):#divide um número n em k partes com um máximo
    if n==0 and k==0: return [[]]
    if k==0 and n!=0: return []
    if (n, maximo, k) not in memo:
        result = []
        for x in range(min(maximo, n), 0, -1):
            result+=[y+[x] for y in divide(n-x, x, k-1)]
        memo[(n,maximo,k)]=result
    return memo[(n,maximo,k)]

def sets(k, maximo):
    result = []
    for x in range(k, maximo*k+1):
        result+=divide(x, maximo, k)
    return result

def count(d, n, k, i):#d dados cujos k maiores somam n (dados de 1 até i)
    todos = [x+y for y in divide(n, i, k) for x in sets(d-k, y[0])]
    result = 0
    for x in todos:
        result += anagram(d, [x.count(y) for y in range(1, i+1)])
    return result
    



print(count(20, 70, 10, 12))
    
