soma = 0

#quando a = b+1

lista1 = [(5,4)]
while lista1[-1][0]*3+1<=10**9:
    bn = lista1[-1][0]
    hn = lista1[-1][1] 
    lista1.append((7*bn+8*hn-2, 6*bn+7*hn-2))


#quando a = b-1

lista2 = [(17,15)]
while lista2[-1][0]*3-1<=10**9:
    bn = lista2[-1][0]
    hn = lista2[-1][1] 
    lista2.append((7*bn+8*hn+2, 6*bn+7*hn+2))

perimetros1 = [x[0]*3+1 for x in lista1[:-1]]
perimetros2 = [x[0]*3-1 for x in lista2[:-1]]

print (sum(perimetros1)+sum(perimetros2))



#Esse algoritmo é lindo :D
