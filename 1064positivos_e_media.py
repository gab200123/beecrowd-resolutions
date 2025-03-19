positivos = [float(input()) for _ in range(6)]
total_positivos = 0
soma_dos_positivos = 0

for n in positivos:
    if n > 0:
        total_positivos += 1
        soma_dos_positivos += n

print('{} valores positivos'.format(total_positivos))
print('{:.1f}'.format(soma_dos_positivos / total_positivos))
