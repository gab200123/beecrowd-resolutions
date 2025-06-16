n = int(input())

for i in range(0,n):
    divide = list(map(int, input().split()))
    if divide[1] == 0:
        print('divisao impossivel')
        continue

    else:
        divisao = divide[0] / divide[1]
        print(divisao)
