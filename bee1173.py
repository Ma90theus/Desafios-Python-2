valores = []
entrada = int(input())

for valor in range(0,10):
    valores.append(entrada)
    entrada = entrada * 2

for valor in range(0,10):
    print("N[{}] = {}".format(valor,valores[valor]))