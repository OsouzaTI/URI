par = 0
impar = 0
negativo = 0
positivo = 0
for i in range(5):
	n = float(input())
	if n%2==0:par += 1
	else: impar += 1
	if n > 0:positivo += 1
	elif n < 0: negativo += 1
print('%i valor(es) par(es)\n%i valor(es) impar(es)\n%i valor(es) positivo(s)\n%i valor(es) negativo(s)'%(par,impar,positivo,negativo))