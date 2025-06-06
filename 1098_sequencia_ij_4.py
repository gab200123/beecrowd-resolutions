i = 0.0

while i <= 2:
    j = 1    
    for _ in range(3):
        usado = i + j
        if float(i).is_integer():
            print(f'I={int(i)} J={int(usado)}')
        else:
            print(f'I={i:.1f} J={usado:.1f}')
        j += 1 
    i = round(i + 0.2, 1)  
