def checa(valores):
        add = int(input())
        valores.append(add)

        if valores[-1] < 0:
            if valores[-1] % 2 == 0:
                return 'EVEN NEGATIVE'
            
            return 'ODD NEGATIVE'
        
        elif valores[-1] > 0:
            if valores[-1] % 2 == 0:
                return 'EVEN POSITIVE'
            
            return 'ODD POSITIVE'
        
        return 'NULL'
        
        
entrada = int(input())
valores = []
for i in range(entrada):
    veremos = checa(valores)
    print(veremos)
