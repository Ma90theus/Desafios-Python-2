x = int(input())
if x>= 1 and x <=1000:
    kmtotal = 0
    for i in range(0,x):
        kmatual = 0
        tempo,velocidade = input().split(" ")
        t = int(tempo)
        v = int(velocidade)
        if t >= 1 and t <= 100 and v >= 0 and v <= 120:
            kmatual = v * t
            kmtotal = kmtotal + kmatual
print(kmtotal)