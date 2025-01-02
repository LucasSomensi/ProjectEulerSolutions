from math import log

def numeros(N):
    return [bin(x)[2:] for x in range(0, 2**N)]

def teste(candidato, N):
    candidato = candidato[-N+1:]+candidato
    for x in numeros(N):
        if x not in candidato: return False
    return True


N = 8
candidatos = ['0'*N]

while len(candidatos[0])!=2**N:
    temp = []
    for y in candidatos:
        for x in ['0', '1']:
            if y[-N+1:]+x not in y: temp.append(y+x)
    candidatos = temp

print (sum([int(x, 2) for x in candidatos if teste(x, N)]))
