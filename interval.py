num = int(input())
vet = [10001]
inp = 0

for i in range(num):
    num2 = int(input())
    if 10 <= num2 <= 20:
        inp += 1

print("%d in"% inp)
print("%d out"% (num2-inp))