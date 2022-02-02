x = int(input())
if x > 0 and x < 13: 
    aux = 1
    for i in range(x,0,-1):
        aux = aux * i
print(aux)