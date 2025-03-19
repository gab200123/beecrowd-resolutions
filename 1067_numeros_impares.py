num = int(input())

impar = num % 2 == 1

if impar:
  for i in range(1, num+1, 2):
    print(i)

else:
  for i in range(1, num, 2):
    print(i)
