#The numbers should be entered with spaces to distinguish them as separate.
n = list(map(float, input().split()))
i = 0
pos = 0
neg = 0
cont = 0
paridade = 0
par = 0
impar = 0

while i < len(n):
  paridade = n[i] % 2
  if n[i] > 0 and paridade == 0:
    pos += 1
    par += 1

  elif n[i] > 0 and paridade > 0:
    pos += 1
    impar += 1

  elif n[i] < 0 and paridade == 0:
    neg += 1
    par += 1

  elif n[i] < 0 and paridade > 0:
    neg += 1
    impar += 1

  else:
    par += 1

  i += 1

print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{pos} valor(es) positivo(s)')
print(f'{neg} valor(es) negativo(s)')
