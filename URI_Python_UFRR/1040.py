linha1 = input().split(' ')
n1, n2, n3, n4 = linha1
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
mediaI = ( n1*2 + n2*3 + n3*4 + n4*1 )/10
print('Media: %.1f' %mediaI)
if mediaI >= 7:
	print('Aluno aprovado.') 
elif mediaI < 5:
	print('Aluno reprovado.')
else:
	print('Aluno em exame.')
	n = float(input())
	print('Nota do exame: %.1f'%n)
	mediaII = (n + mediaI)/2
	if mediaII >= 5: print('Aluno aprovado.')
	else: print('Aluno reprovado.')
	print('Media final: %.1f'%mediaII)





