num = int(input())
vet = []

for i in range(num):
    xy = input().split(' ')
    x = int(xy[0])
    y = int(xy[1])
    if y!=0:
        vet.append(x/y)
    else:
        vet.append(100101)	



for i in range(num):
    if vet[i]!=100101:
        print("%.1lf"% vet[i])
    else:
        print("divisao impossivel")

