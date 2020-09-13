notas = input().split(' ')
n1 = float(notas[0])
n2 = float(notas[1])
n3 = float(notas[2])
n4 = float(notas[3])

media = ((n1*2)+(n2*3)+(n3*4)+n4)/10.0


print('Media: %.1f' % (media))
if media >= 7.0:
##print('Media: ',media)
    print('Aluno aprovado.')
elif media < 5.0:
#print('Media: ',media)
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    n5 = float(input())
    print('Nota do exame: %.1f'%(n5))
    novaMedia = (media + n5)/2.0
    if novaMedia  >= 5.0:
        print('Aluno aprovado.')
        print('Media final: %.1f'% (novaMedia))
    else:
        print('Aluno reprovado.')
        print('Media final: %.1f'% ( novaMedia))