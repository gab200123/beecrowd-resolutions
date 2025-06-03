def bora(valor):
    for i in range(2,valor+2,2):
        quadrado = i ** 2
        print(f'{i}^2 = {quadrado}')    

valor = int(input())
par = 0

if valor % 2 == 0:
    bora(valor)

else:
    valor -= 1
    bora(valor)
