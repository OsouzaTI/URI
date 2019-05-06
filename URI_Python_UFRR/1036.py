linha1 = input().split(" ")
a, b, c = linha1
a = float(a)
b = float(b)
c = float(c)
delta = b**2 - 4 * a * c
if delta < 0 or a == 0:
	print('Impossivel calcular')
elif delta > 0 and (a != 0):
	print('R1 = %.5f' %( (-b + (delta)**(1/2))/ (2*a) ))
	print('R2 = %.5f' %( (-b - (delta)**(1/2))/ (2*a) ))
