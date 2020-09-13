
pos = 0
teste=0
for i in range(100):
    num = int(input())
    if num > teste:
        teste=num 
        pos = i+1

print("{0}\n{1}".format(teste,pos))
