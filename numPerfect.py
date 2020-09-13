num = int(input())
acm = 0
for i in range(num):
    x = int(input())
    acm=0
    for i in range(1,x):
        if x % i == 0:
            acm+=i;	
    if acm == x:
        print("%d eh perfeito"% x)
    else: 
        print("%d nao eh perfeito"% x)	
