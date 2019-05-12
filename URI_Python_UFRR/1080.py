maior = 0
indice = 0
val = []
for i in range(100):
    val.append(int(input()))

for j in range(100):
    if val[j] > maior:
        maior = val[j]
        indice = j+1

print(maior)
print(indice)
