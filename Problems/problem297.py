memo = {}

def M(n):
    if n==1: return 0
    if n==2: return 1
    a=1
    b=2
    while b<n:
        a, b = b, a+b
    return a


def S(n):
    if n==1: return 0
    if n in memo: return memo[n]
    temp = M(n)
    memo[n] = S(temp)+S(n-temp)+n-temp
    return memo[n]


print (S(100000000000000000))
