notas = input().split(' ')
x = float(notas[0])
y = float(notas[1])
	

if x==0.0 and y==0.0:
    print("Origem")
else:
    if x>0.0 and y>0.0:
        print("Q1")
    
    else:
        if x>0.0 and y<0.0:
            print("Q4")
        
        else:
            if x<0.0 and y>0.0:
                print("Q2")
            else:
                if x<0.0 and y<0.0:	
                    print("Q3")
                
                if x==0.0:
                    print("Eixo Y")
                
                if y==0.0:
                    print("Eixo X")
                	
print("\n")