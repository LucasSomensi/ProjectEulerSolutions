from math import sqrt

def totient(n):
    fatores = []
    result = n
    k = 2
    while k<=sqrt(n):
        if n%k==0: fatores.append(k)
        while n%k==0: n//=k
        k+=1
    if n!=1: fatores.append(n)
    for x in fatores:
        result*=(x-1)
        result//=x
    return result

d=2*3*5*7*11*13*17

while totient(d)/(d-1) >= 15499/94744:
    d+=2*3*5*7*11*13*17


print (d)
