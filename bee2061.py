a,b = input().split(" ")
abas = int(a)
acao = int(b)
fechado = 2
antigo = 1
for i in range(0,acao):
    evento = input()
    if evento == "fechou" or evento == "clicou":
        if evento == "fechou":
            abas = abas + fechado - antigo
        elif evento == "clicou":
            abas = abas - antigo
print(abas)