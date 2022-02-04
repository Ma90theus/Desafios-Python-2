valores = []
valores_convertidos = []

#Armazenar no vetor
valores = input().split(" ")  
for i in range(0,4):
    valores_convertidos.append(int(valores[i]))

#Busco no vetor a posição do meu 1
for valor in range(0,4):
    if valores_convertidos[valor] == 1:
        print(valor+1)
