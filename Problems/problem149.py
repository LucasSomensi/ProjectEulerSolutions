#!/usr/bin/python
import sys

generator=[(100003-200003*x+300007*x**3)%1000000-500000 for x in xrange(1, 56)]
while len(generator)!=4000000:
    generator.append((generator[-24]+generator[-55]+1000000)%1000000-500000)

matrix = [generator[2000*x:2000*x+2000] for x in xrange(0, 2000)]


memo={}

def solve(l, c, d):
    if not 0<l+d[0]<len(matrix):
        return matrix[l][c]
    if not 0<c+d[1]<len(matrix[0]):
        return matrix[l][c]
    if not memo.has_key(l) or not memo[l].has_key((c, d)):
        if not memo.has_key(l): memo[l]={}
        a=solve(l+d[0], c+d[1], d)
        if a<=0:
            memo[l][(c, d)]=matrix[l][c]
            return matrix[l][c]
        else:
            memo[l][(c, d)]=matrix[l][c]+a
            return matrix[l][c]+a
    return memo[l][(c,d)]


best=0
current=(0,0, (0,0))
for l in xrange(len(matrix)):
    print l, best, current
    if memo.has_key(l-2): del(memo[l-2])
    for c in xrange(len(matrix[0])):
        for d in [(-1,-1),(-1,0),(-1,1),(0,-1)]:
            a=solve(l, c, d)
            if a>best:
                best=a
                current=(l, c, d)


memo={}

for l in xrange(len(matrix)-1,-1 ,-1):
    print l, best, current
    if memo.has_key(l+2): del(memo[l+2])
    for c in xrange(len(matrix[0])-1, -1, -1):
        for d in [(0,1),(1,-1),(1,0),(1,1)]:
            a=solve(l, c, d)
            if a>best:
                best=a
                current=(l, c, d)


print best
print current
