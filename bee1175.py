vetor_certo = []
vetor_contrario = []
for i in range(0,20):
    vetor_certo.append(input())
for i in range(20,0,-1):
    aux = vetor_certo.pop()
    vetor_contrario.append(aux)
for i in range(0,20):
    print("N[{}] = {}".format(i,vetor_contrario[i]))