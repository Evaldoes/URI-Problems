num = int(input())

vet = []
menor = 999999
pos =0

teste = input().split(' ')
for i in range(num):
    vet.append(int(teste[i]))
    if vet[i] < menor:
        menor = vet[i]
        pos = i

print("Menor valor: %d"% menor)
print("Posicao: %d"% pos)
