n = int(input())
coelho = 0
sapo = 0
rato = 0
total = 0

for i in range(0, n):
    qtd, especie = input().split()
    qtd = int(qtd)
    especie = especie.lower()

    if especie == 'c':
        coelho += qtd

    elif especie == 's':
        sapo += qtd

    elif especie == 'r':
        rato += qtd

    else:
        i -= 1

    total += qtd

p_coelho = (coelho *100) / total
p_sapo = (sapo * 100) / total
p_rato = (rato * 100) / total

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelho}')
print(f'Total de ratos: {rato}')
print(f'Total de sapos: {sapo}')
print(f'Percentual de coelhos: {p_coelho:.2f} %')
print(f'Percentual de ratos: {p_rato:.2f} %')
print(f'Percentual de sapos: {p_sapo:.2f} %')
