numeros = []

while 0 not in numeros:
    numeros = []
    somando = []
    somado  = 0
    numeros = list(map(int, input().split()))
    numeros.sort()

    for i in range(numeros[0], numeros[-1]+1):
        somado += i
        somando.append(i)

        if i <= 0:
            quit()

    print(f'{" ".join(map(str, somando))} Sum={somado}')
