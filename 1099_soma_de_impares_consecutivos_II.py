n = int(input())
soma = 0

for _ in range(0, n):
    entrada = input()
    valores = list(map(int, entrada.split()))
    valores.sort()

    v1, v2 = map(int, valores)

    if v1%2 == 0:
        for i in range(v1+1,v2,2):
                soma += i
    else:
        for i in range(v1+2,v2,2):
            soma += i
    print(soma)
    soma = 0
