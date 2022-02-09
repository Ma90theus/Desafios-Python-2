x = int(input())
for i in range(0,x):
    j = 0
    soma = 0
    valores = input().split(" ")
    a  = int(valores[0])
    contagem = int(valores[1])
    while j < contagem: #Quero que o laço fique existindo ate ele encontrar a quanditade correta de valores impares
        if a % 2 != 0:
            soma = soma + a
            j = j + 1 #Só vai para a proxima iteração se achar o valor impar
        a = a + 1 #incremento o valor de a para que busque o p´roximo valor,e se ele for impar será operado o if
    print(soma)



    