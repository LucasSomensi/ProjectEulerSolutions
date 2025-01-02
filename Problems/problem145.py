def reverse(n):
    if n%10 == 0: return False
    i=len(str(n))-1
    result=0
    while n!=0:
        result+=(n%10)*10**i
        n=n//10
        i-=1
    return result

def reversible(n):
    soma = n + reverse(n)
    while soma!=0:
        if soma%2==0: return False
        soma = soma//10
    return True

def build(candidate):
    if '_' not in candidate:
        if reversible(int(candidate)): return [candidate]
        else: return []
    start = ''
    end = ''
    x=0
    while candidate[x]!='_':
        start+=candidate[x]
        end = candidate[-1-x] + end
        x+=1
    result = []
    if len(candidate)-2*len(start) == 1:
        for a in range(0, 10):
            result+=build(start+str(a)+end)
        return result
    intervalo = range(1,10)
    if len(start)!=0: intervalo = range(0, 10)
    for a in intervalo:
        for b in intervalo:
            soma = 0
            for x in range(len(start)):
                soma += int(start[x]) + int(end[-1-x])
                soma = soma//10
            soma += a+b
            #print (start+str(a)+'_'*(len(candidate)-2*len(start)-2)+str(b)+end)
            if soma%2==1: result += build(start+str(a)+'_'*(len(candidate)-2*len(start)-2)+str(b)+end)
    return result
            
    
        

lista=[]
for x in range(2, 9):
    print (x)
    lista+=build('_'*x)
print (len(lista))
    
