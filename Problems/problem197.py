from decimal import *
from math import *

a = Decimal('-1.00000000000000000000')
print (a)
for x in range(1, 100000):
    a, b = floor(2**(Decimal('30.403243784')-a**2))*Decimal('0.000000001'), a
    print (a+b)
