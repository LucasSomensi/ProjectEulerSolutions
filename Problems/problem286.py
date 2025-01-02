#é necessário testar os candidatos a q na mao

from decimal import *
import sys

memo={}

def produto(lista):
    result = 1
    for x in lista:
        result*=x
    return result

def P(q, n, k):
    if k>n: return 0
    if k==0: return produto([Decimal(x)/q for x in range(1, n+1)])
    if k==n: return produto([1-Decimal(x)/q for x in range(1, n+1)])
    if (q,n,k) not in memo:
        memo[(q,n,k)]=(Decimal(n)/q)*P(q, n-1, k)+(1-Decimal(n)/q)*P(q, n-1, k-1)
    return memo[(q,n,k)]
    



print (P(Decimal(sys.argv[1]), 50, 20))
