valores = []
#recebendo os valores das gangorras
valores = input().split(" ")
p1 = int(valores[0])
c1 = int(valores[1])
p2 = int(valores[2])
c2 = int(valores[3])
if p1 >= 10 and p1 <= 100 and p2 >= 10 and p2 <= 100 and c1 >= 10 and c1 <= 100 and c2 >= 10 and c2 <= 100:
    esquerda = p1 * c1
    direita = p2 * c2
    if direita == esquerda:
        valor = 0
    elif direita > esquerda:
        valor = 1
    else:
        valor = -1
    print(valor)
