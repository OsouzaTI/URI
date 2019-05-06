tab = [
	(4.00,4.50,5.00,2.00,1.50)
]
linha1 = input().split(' ')
n, q = linha1
n = int(n)
q = int(q)
#print('item {} tem o valor de {}'.format(tab[0][0],tab[1][0]))
print('Total: R$ {:.2f}'.format( q * tab[0][n-1] ))