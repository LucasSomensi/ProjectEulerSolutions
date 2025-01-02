lista1 = [(-1,0)]
lista2 = [(1,0)]
lista3 = [(-7, 2)]
lista4 = [(7,2)]
lista5 = [(-2,-3)]
lista6 = [(2, -3)]
lista7 = [(-5, -4)]
lista8 = [(5, -4)]
lista9 = [(14,5)]

for x in range(0, 11):
    lista1.append((-9*lista1[-1][0]+20*lista1[-1][1]+28, 4*lista1[-1][0]-9*lista1[-1][1]-14))
    lista2.append((-9*lista2[-1][0]+20*lista2[-1][1]+28, 4*lista2[-1][0]-9*lista2[-1][1]-14))
    lista3.append((-9*lista3[-1][0]+20*lista3[-1][1]+28, 4*lista3[-1][0]-9*lista3[-1][1]-14))
    lista4.append((-9*lista4[-1][0]+20*lista4[-1][1]+28, 4*lista4[-1][0]-9*lista4[-1][1]-14))
    lista5.append((-9*lista5[-1][0]+20*lista5[-1][1]+28, 4*lista5[-1][0]-9*lista5[-1][1]-14))
    lista6.append((-9*lista6[-1][0]+20*lista6[-1][1]+28, 4*lista6[-1][0]-9*lista6[-1][1]-14))
    lista7.append((-9*lista7[-1][0]+20*lista7[-1][1]+28, 4*lista7[-1][0]-9*lista7[-1][1]-14))
    lista8.append((-9*lista8[-1][0]+20*lista8[-1][1]+28, 4*lista8[-1][0]-9*lista8[-1][1]-14))
    lista9.append((-9*lista9[-1][0]+20*lista9[-1][1]+28, 4*lista9[-1][0]-9*lista9[-1][1]-14))




lista = [x[1] for x in lista1+lista2+lista3+lista4+lista5+lista6+lista7+lista8+lista9 if x[1]>0]
lista = list(set(lista))
lista.sort()

print (sum(lista[:30]))
