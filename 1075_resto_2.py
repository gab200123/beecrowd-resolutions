def resta(valor, indice):
    dividido = indice % valor
    if dividido == 2:
        return indice
    else:
        return
    
valor = int(input())
for i in range(1,10000):
    resultado = resta(valor, i)

    if resultado is not None:
        print(resultado)
        
