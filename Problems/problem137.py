lista1 = [(-1,0)]
lista2 = [(1,0)]
lista3 = [(-2, -1)]

for x in range(0, 11):
    lista1.append((-9*lista1[-1][0]-20*lista1[-1][1]-4, -4*lista1[-1][0]-9*lista1[-1][1]-2))
    lista2.append((-9*lista2[-1][0]-20*lista2[-1][1]-4, -4*lista2[-1][0]-9*lista2[-1][1]-2))
    lista3.append((-9*lista3[-1][0]-20*lista3[-1][1]-4, -4*lista3[-1][0]-9*lista3[-1][1]-2))



def merge(lista1, lista2):
    if lista1==[]: return lista2
    if lista2==[]: return lista1
    if lista1[0]<=lista2[0]: return lista1[0:1]+merge(lista1[1:], lista2)
    if lista2[0]<lista1[0]: return lista2[0:1]+merge(lista1, lista2[1:])

lista = [x[1] for x in lista1+lista2+lista3 if x[1]>0]
lista.sort()

print (lista[14])
