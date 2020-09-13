num = int(input())
vet = []   
cont = 0
k = 0
aux = 0
for i in range(num):
    xy = input().split(' ')
    x = int(xy[0])
    y = int(xy[1])
    if x>y:
        aux=x
        x=y
        y=aux
    for i in range(x,y):

        if i%2 !=0:
            if i != x:
                cont = cont + i
    vet.append(cont)
    cont=0


for i in range(num):
    print(vet[i])
