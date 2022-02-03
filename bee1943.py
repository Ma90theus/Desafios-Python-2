posicoes = ["1","3","5","10","25","50","100"]
colocado = int(input())
if colocado >= 1 and colocado <= 100:
    for i in range(0,len(posicoes)):
        if colocado == int(posicoes[i]):
            atual = posicoes[i]
        elif colocado > int(posicoes[i]):
            atual = posicoes[i + 1]
print("Top {}".format(atual))