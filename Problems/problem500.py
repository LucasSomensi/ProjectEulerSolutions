from math import log
from math import ceil
from math import floor


target = 500500
nprimes = target

#finding the primes with a sieve
def f(n):
    x = n
    for i in range(10):
        x = n*log(x)
    return ceil(x)

candidates = [False]*2 + [True]*f(nprimes)
primes = []

for x in range(len(candidates)):
    if (candidates[x]==True):
        primes.append(x)
        for y in range(2*x, len(candidates), x):
            candidates[y] = False
primes = primes[0:nprimes]
print("terminou primos")


#initial distribution the numbers

temp = list(map(lambda x: ceil((log(log(x))-log(2))/log(2)), primes))
result = list(map(lambda x: temp[-1]-temp[x], range(nprimes)))
while (sum(result)>target): result = list(map(lambda x: x if x==0 else x-1, result))
while (sum(result)+nprimes)<target: result = list(map(lambda x: x+1, result))
for x in range(target-sum(result)): result[x]+=1
result[0]+=target-sum(result)

print("checksum", sum(result))

#minimizing the number

constant = log(2)
primelogs = list(map(lambda x: log(log(x)), primes)) 

done = True
count = 0

while done:
    done = False
    count+=1
    print(count)
    current = sorted(range(nprimes), key=(lambda i: -(primelogs[i]+constant*(result[i]-1))))
    possible =sorted(range(nprimes), key=(lambda i: primelogs[i]+constant*result[i]))
    i = 0
    while (primelogs[current[i]]+constant*(result[current[i]]-1))>(primelogs[possible[i]]+constant*result[possible[i]]):
        done = True
        result[current[i]]-=1
        result[possible[i]]+=1
        i+=1



#printing the number with modular exponentiation


def modular_multiplicative_inverse(a, m):
    q = [0,0]
    r = [m, a]
    s = [1, 0]
    t = [0, 1]
    while (r[-1]!=0):
        q.append(r[-2]//r[-1])
        r.append(r[-2]-q[-1]*r[-1])
        s.append(s[-2]-q[-1]*s[-1])
        t.append(t[-2]-q[-1]*t[-1])
    return t[-2]


def expmod(prime, n, modulo):
    result = prime%modulo
    for x in range(n): result = (result**2)%modulo
    result = (result*modular_multiplicative_inverse(prime%modulo, modulo))%modulo
    return result

def expmod13(prime, n, modulo):
    result = 1
    for x in range(2**n-1): result = (result*(prime%modulo))%modulo
    return result

    
def expand(result_list, modulo):
    result = 1
    for x in range(nprimes):        
        if (not primes[x]==13): result=(result*expmod(primes[x], result_list[x], modulo))%modulo
        else: result=(result*expmod13(primes[x], result_list[x], modulo))%modulo
    return result



print(expand(result, 500500507))
