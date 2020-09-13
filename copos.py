def movimenta(pos, jogada):
  if jogada == 1:
    valor1, valor2 = 'A', 'B'
  elif jogada == 2:
    valor1, valor2 = 'B', 'C'
  elif jogada == 3:
    valor1, valor2 = 'A', 'C'
  if pos == valor1:
    return valor2
  elif pos == valor2:
    return valor1
  else:
    return pos



num = int(input())
pos = input()

for i in range(num):
  jogada = int(input())
  pos = movimenta(pos, jogada)

print(pos)