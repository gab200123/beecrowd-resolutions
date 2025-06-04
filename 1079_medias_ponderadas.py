def media(valor):
    media = (valor[0] * 2) + (valor[1] * 3) + (valor[2] * 5)
    media_ponderada = media / 10
    return round(media_ponderada, 1)

n = int(input())
valor = []
for i in range(0, n):
    recebe = input()
    valor = list(map(float, recebe.split()))
    mostra = media(valor)
    print(mostra)
