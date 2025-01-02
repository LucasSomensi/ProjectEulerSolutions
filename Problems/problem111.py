import random

def concat(a,b):
    return [x for x in a]+[x for x in b]

def teste(p):
    if p%2==0: return False
    if p%3==0: return False
    for a in [random.randint(2, p-1) for y in range(1,100)]:
        if pow(a, p-1, p)!=1: return False
    return True

def moldes(holes, sequencia):
    if holes==0: return [sequencia]
    result = []
    for a in range(0, len(sequencia)-holes+1):
        result+=[sequencia[:a]+'_'+y for y in moldes(holes-1, sequencia[a+1:])]
    return result

def fill(sequencia, exc):
    if sequencia[0]=='0': return []
    if '_' not in sequencia: return [sequencia]
    intervalo = concat(range(0, exc),range(exc+1, 10))
    if sequencia[0]=='_': intervalo = concat(range(1, exc),range(exc+1, 10))
    result = []
    for a in intervalo:
        result+=fill(sequencia[:sequencia.find('_')]+str(a)+sequencia[sequencia.find('_')+1:], exc)
    return result

def todos(n, d, k):
    result = []
    for x in moldes(n-k, str(d)*n):
        result+=fill(x, d)
    return result

def primos(n, d, k):
    return [int(x) for x in todos(n,d,k) if teste(int(x))]

def M(n, d):
    k=n
    while len(primos(n, d, k))==0:
        k-=1
    return k

def N(n, d):
    return len(primos(n,d,M(n,d)))

def S(n, d):
    return sum(primos(n,d,M(n,d)))

def sumoval(n):
    return sum([S(n,x) for x in range(0, 10)])
        

print (sumoval(10))
