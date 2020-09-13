xy = input().split(' ')
x = int(xy[0])
y = int(xy[1])
vet = [10000]
k=0

while x!=y:
    if x > y:
        vet.append(1)
    else:
        vet.append(0)
    k+=1
    xy = input().split(' ')
    x = int(xy[0])
    y = int(xy[1])

for i in range(len(vet)):
    if vet[i] == 1:
        print("Decrescente")
    else:
        print("Crescente")