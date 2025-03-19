num = int(input())
i = 0

impar = num % 2 == 1

if impar:
  while i < 6:
    print(num)
    num += 2
    i += 1

else:
  num += 1
  while i < 6:
    print(num)
    num += 2
    i +=1
