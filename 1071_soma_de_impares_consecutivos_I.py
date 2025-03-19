num = [int(input()) for _ in range(2)]
num.sort()
soma = 0

if num[0] % 2 == 1:
  for i in range(num[0], num[1], +2):
    soma = 0 + i
  print(soma)

else:
  for i in range(num[0]+1, num[1], +2):
    soma = 0 + i
  print(soma)
