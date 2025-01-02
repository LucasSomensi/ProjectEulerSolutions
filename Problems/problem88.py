from math import *

dic={}

def divide_stub(n):
    if n==1: return []
    result = [[n]]
    for a in range(2, int(ceil(n**0.5))+1):
        if n%a==0: result+=[[a]+x for x in divide(n//a)]
    return result
        
        
def divide(n):
    result=divide_stub(n)
    for x in result: x.sort()
    i=0
    while i<len(result):
        if result[i] in result[:i]:
            del(result[i])
            i-=1
        i+=1
    result.sort()
    return result

def mult(lista):
    result=1
    for x in lista: result*=x
    return result
    
numeros = {}
n=3
while True in [n not in numeros for n in range(2, 12001)]:
    for x in divide(n):
        if len(x)+(mult(x)-sum(x)) not in numeros and len(x)+(mult(x)-sum(x))>1:
            numeros[len(x)+(mult(x)-sum(x))]=n
    print (n)
    n+=1

soma = []
for x in range(2, 12001):
    if numeros[x] not in soma: soma.append(numeros[x])

print(soma)
print(sum(soma))
