import math

def problem202(n):
    result = 0
    if (n+3)%2!=0: return 0
    a = (n+3)//2
    b = (2*a)%3
    if b==0: b+=3
    while a-b>b:
        c = a-b
        if math.gcd(a,b,c)==1:
            result+=2
        b+=3
    return result

print(problem202(11))
print(problem202(1000001))
print(problem202(12017639147))
