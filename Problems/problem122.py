#!/usr/bin/python
import sys

#warning: uses 2GB of RAM

limit=int(sys.argv[1])
solution=[0]+[None]*(limit)

current=[[1]]
while current!=[]:
    new=[]
    for x in current:
        if solution[x[-1]]==None:
            solution[x[-1]]=(len(x)-1)
            print x[-1], ': ', x, len(x)-1
            print solution.count(None), sum([z for z in solution if z!=None])
            if None not in solution:
                print solution, sum(solution)
                exit()
    for x in current:
        for y in x:
            if x[-1]+y<=limit: new.append(x+[x[-1]+y])
    current=new

print solution
        



