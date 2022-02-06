valores = []
valores_flutuantes = []

for i in range(0,4):
    aux = float(input())
    valores.append(aux)

for i in range(0,len(valores)):
    valores_flutuantes.append(float(valores[i]))
    if valores_flutuantes[i] <= 10:
        print("A[{}] = {:.1f}".format(i,valores_flutuantes[i]))