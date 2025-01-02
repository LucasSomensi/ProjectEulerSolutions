#!/usr/bin/python
import sys
import string

def connected(matrix):
    visited=[False]*len(matrix)
    current=[0]
    visited[0]=True
    while current!=[]:
        new=[]
        for x in current:
            for y in xrange(0, len(matrix[x])):
                if matrix[x][y]!=0 and visited[y]==False:
                    visited[y]=True
                    new.append(y)
        current=new
    return visited.count(True)==len(matrix)

def all_edges(matrix):
    result=[]
    for x in xrange(len(matrix)):
        for y in xrange(x+1, len(matrix)):
            if matrix[x][y]!=0: result.append((x, y, matrix[x][y]))
    return result


def quicksort(edges):
    if len(edges)<=1: return edges
    pivot=edges[0][2]
    return quicksort([x for x in edges if x[2]>pivot])+\
           [x for x in edges if x[2]==pivot]+\
           quicksort([x for x in edges if x[2]<pivot])


def reduc(matrix):
    edges=quicksort(all_edges(matrix))
    for x in edges:
        if connected(matrix[:x[0]]+
                     [matrix[x[0]][:x[1]]+[0]+matrix[x[0]][x[1]+1:]]+
                     matrix[x[0]+1:x[1]]+
                     [matrix[x[1]][:x[0]]+[0]+matrix[x[1]][x[0]+1:]]+
                     matrix[x[1]+1:]
                     ):
            matrix[x[0]][x[1]]=0
            matrix[x[1]][x[0]]=0



def myprint(matrix):
    for x in matrix:
        for y in x:
            print y,'\t',
        print ''


def weight(matrix):
    result=0
    for x in matrix:
        result+=sum(x)
    result/=2
    return result
    


matrix=[]
f=open('/home/lucas/network.txt', 'r')
line=f.readline()
while line!='':
    matrix.append(eval(string.replace('['+line[:-2]+']', '-', '0')))
    line=f.readline()





a=weight(matrix)
reduc(matrix)
print a-weight(matrix)
        
