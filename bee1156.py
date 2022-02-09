a = 1
b = 1
soma = 0
for i in range(1,40,2):
    opr = a/b
    soma = soma + opr
    a  = a  + 2
    b = b * 2
print("{:.2f}".format(soma))