#this code could benefit from memoization, but i am too lazy to implement it myself
from decimal import *

def cut(start, x):
    result=start[:]
    result[x]-=1
    for y in range(x+1, len(start)):
        result[y]+=1
    return result

def EP(start):
    if start==[0,0,0,0,1]: return Decimal(1)
    result = Decimal(0)
    if sum(start)==1: result+=Decimal(1)
    for x in range(0, 5):
        if start[x]!=0:
            result+=start[x]*EP(cut(start, x))/sum(start)
    return result

print(EP([1,0,0,0,0]))
