num = [int(input()) for _ in range(2)]
num.sort()
soma = 0

for i in range(num[0] + 1, num[1]):
    if i % 2 !=0:
        soma += i

print(soma)
