linha1 = input().split(' ')
a, b, c = map(float, linha1)
if (a > b > c) or (a == b > c) or (a == b == c):
    a_ = a
    b_ = b
    c_ = c
elif (a > c > b) or (a == c > b) or (a > c == b):
    a_ = a
    b_ = c
    c_ = b
elif (c > a > b) or (c == a > b) or (c > a == b):
    a_ = c
    b_ = a
    c_ = b
elif (c > b > a) or (c == b > a) or (c > b == a):
    a_ = c
    b_ = b
    c_ = a
elif (b > c > a) or (b == c > a) or (b > c == a):
    a_ = b
    b_ = c
    c_ = a
elif (b > a > c) or (b == a > c) or (b > a == c):
    a_ = b
    b_ = a
    c_ = c
    
if a_ >= b_ + c_:print('NAO FORMA TRIANGULO')
else:
    if (a_**2) == (b_**2) + (c_**2):print('TRIANGULO RETANGULO')
    if (a_**2) > (b_**2) + (c_**2):print('TRIANGULO OBTUSANGULO')
    if (a_**2) < (b_**2) + (c_**2):print('TRIANGULO ACUTANGULO')
    if a_==b_==c_:print('TRIANGULO EQUILATERO')
    elif a_==b_:print('TRIANGULO ISOSCELES')
    elif a_==c_:print('TRIANGULO ISOSCELES')
    elif b_==c_:print('TRIANGULO ISOSCELES')