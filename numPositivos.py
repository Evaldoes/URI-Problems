list = []
cont = 0

for i in range(6):
    list.append(float(input()))
    if list[i] > 0:
        cont += 1

print('%s valores positivos'% cont)


