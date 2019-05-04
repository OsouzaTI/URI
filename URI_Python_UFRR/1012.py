linha1 = input().split(" ")

pi = 3.14159
A, B, C = linha1

a_ = (float(A) * float(C))/2
b_ = pi * (float(C)**2)
c_ = ((float(A) + float(B))*float(C))/2
d_ = float(B)**2
e_ = float(A) * float(B)

print('TRIANGULO: {:.3f}'.format(a_))
print('CIRCULO: {:.3f}'.format(b_))
print('TRAPEZIO: {:.3f}'.format(c_))
print('QUADRADO: {:.3f}'.format(d_))
print('RETANGULO: {:.3f}'.format(e_))