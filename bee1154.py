x = 0
estado = True
cont = 0
soma = 0
while estado == True:
    x = int(input())
    if x < 0:
        estado = False
    else:
        soma = soma + x
        cont = cont + 1
media = (soma/cont)
print("{:.2f}".format(media))