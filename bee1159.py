x = True

while x == True:
    j = 0
    soma = 0
    y = int(input())
    if y == 0:
        x = False
    else:
        while j < 5:
            if y % 2 == 0:
                soma = soma + y
                j = j + 1
            y = y + 1
        print(soma)
