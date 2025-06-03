qtd = int(input())
entrada = None
valor = []
cont = 0
n_cont = 0
tenta = 0

for i in range(0,qtd):
    entrada = int(input())
    valor.append(entrada)

    if 10 <= valor[tenta] <= 20:
        cont += 1

    else:
        n_cont += 1

    tenta += 1

print(f'{cont} in')
print(f'{n_cont} out')
