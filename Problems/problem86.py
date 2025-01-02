m=2
limite = 1818


def gcd(a,b):
    if a==0: return b
    return gcd(b%a, a)

def teste(a,e,limite):
    result = []
    if a>limite: return []
    c=1
    while c<=e//2:
        b=e-c
        if b>limite:
            c+=1
            continue
        if c>limite: break
        if a**2+e**2<=(a+b)**2+c**2 and a**2+e**2<=(a+c)**2+b**2:
            result.append((a,b,c))
        c+=1
    return result


result=[]
while (max(m**2-1, 2*m)<=limite*2 and min(m**2-1, 2*m)<=limite):
    if m%2==0: n=1
    if m%2==1: n=2
    while n<m:
        if gcd(m,n)==1 and (max((m**2-n**2), 2*m*n)<=limite*2 and min((m**2-n**2), 2*m*n)<=limite):
            d=1
            while (max((m**2-n**2)*d, 2*m*n*d)<=limite*2 and min((m**2-n**2)*d, 2*m*n*d)<=limite):
                result+=teste((m**2-n**2)*d, 2*m*n*d,limite)+teste(2*m*n*d, (m**2-n**2)*d,limite)
                d+=1
        n+=2
    m+=1

#print(result)
print(len(result))

##result2=[]
##for a in range(1, limite+1):
##    for b in range(1, a+1):
##        for c in range(1, b+1):
##            if min((a**2+(b+c)**2)**0.5, (b**2+(a+c)**2)**0.5, (c**2+(a+b)**2)**0.5)%1==0:
##                result2.append((a,b,c))
##
##for x in result2:
##    if x not in result: print(x)

