valores = []
x = int(input())
if x >= 2 and x <= 50:
    for i in range(0,1000):
        for i in range(0,x):
            valores.append(i)

    for i in range(0,1000):
        print("N[{}] = {}".format(i,valores[i]))