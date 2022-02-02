x = int(input())
b = 0
valor = True
while valor == True:
    if b <= x:
        b = int(input())
    else:
        aux = b
        valor = False
contador = 1
soma = x
while soma <= aux:
    contador = contador + 1
    x = x + 1
    soma = soma + x
print(contador)