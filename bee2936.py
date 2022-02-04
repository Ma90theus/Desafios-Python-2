gramas = ["300","1500","600","1000","150"]
soma = 225
for i in range(0,5):
    quantidade = int(input())
    grama = int(gramas[i])
    soma = soma + (grama * quantidade)
print(soma)
