
memounr={}
memores={}

def unr(k, m=(False,False,False)):
    if k==1:
        if m.count(False)>=2: return 0
        if m.count(False)==1: return 1
        if m.count(False)==0: return 3
    if (k, m) not in memounr: 
        memounr[(k,m)]=unr(k-1, (True, m[1], m[2])) + unr(k-1, (m[0], True, m[2])) + unr(k-1, (m[0], m[1], True))
    return memounr[(k,m)]

def res(k, m=(False,False,False)):
    if k==1:
        if m.count(False)>=2 or m[0]==False: return 0
        if m.count(False)==1: return 1
        if m.count(False)==0: return 2
    if (k, m) not in memores: 
        memores[(k,m)]=res(k-1, (True, m[1], m[2])) + res(k-1, (m[0], True, m[2])) + res(k-1, (m[0], m[1], True))
    return memores[(k,m)]

def fat(n):
    if n==0: return 1
    return n*fat(n-1)

def C(n,k):
    if n<k: return 0
    return fat(n)//(fat(k)*fat(n-k))

def quantity(n):
    return sum([(unr(k)*C(n-1,k)+res(k)*C(n-1,k-1))*13**(n-k) for k in range(3, n+1)])

print (hex(sum(quantity(n) for n in range(3, 17))))

