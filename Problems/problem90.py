#!/usr/bin/python
import sys


numbers=['01', '04', '09', '16', '25', '36', '49', '64', '81']

def pick(lista, n):
    if n==0: return [[]]
    result=[]
    for x in xrange(len(lista)-n+1):
        result+=[[lista[x]]+y for y in pick(lista[x+1:], n-1)]
    return result


def test(double):
    die1, die2 = double[0], double[1]
    if not (('0' in die1 and '1' in die2) or ('1' in die1 and '0' in die2)): return False
    if not (('0' in die1 and '4' in die2) or ('4' in die1 and '0' in die2)): return False
    if not (('0' in die1 and ('9' in die2 or '6' in die2)) or (('9' in die1 or '6' in die1) and '0' in die2)): return False
    if not (('1' in die1 and ('9' in die2 or '6' in die2)) or (('9' in die1 or '6' in die1) and '1' in die2)): return False
    if not (('2' in die1 and '5' in die2) or ('5' in die1 and '2' in die2)): return False
    if not (('3' in die1 and ('9' in die2 or '6' in die2)) or (('9' in die1 or '6' in die1) and '3' in die2)): return False
    if not (('4' in die1 and ('9' in die2 or '6' in die2)) or (('9' in die1 or '6' in die1) and '4' in die2)): return False
    if not (('8' in die1 and '1' in die2) or ('1' in die1 and '8' in die2)): return False
    return True




dies = pick(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 6)

print len([(x, y) for x in dies for y in dies if test((x, y))])/2


