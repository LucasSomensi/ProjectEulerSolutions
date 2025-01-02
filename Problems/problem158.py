from math import factorial

def pick(k, n):#pick k out of n
    if k>n: return 0
    return factorial(n)//(factorial(k)*factorial(n-k))

def p(n):
    result = 0
    for k1 in range(0, n-1):
        for k2 in range(0, n-1-k1):
            for a in range(1, 26-k1-k2):
                for b in range(k2+a+1, 27-k1):
                    result+=pick(k1, 26-b)*pick(k2, b-a-1)*pick(n-2-k1-k2, b-k2-2)
    return result



print(max([p(x) for x in range(1, 27)]))
