# -*- coding: utf-8 -*-

s = float(input())
if s >= 0 and s <= 400:
    p = (s*(15/100))
    s = s + p
    print('Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 15 '%(s,p)+'%')
elif s>= 400.01 and s <= 800:
    p = (s*(12/100))
    s = s + p
    print('Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 12 '%(s,p)+'%')
elif s>= 800.01 and s <= 1200:
    p = (s*(10/100))
    s = s + p
    print('Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 10 '%(s,p)+'%')
elif s>= 1200.01 and s <= 2000:
    p = (s*(7/100))
    s = s + p
    print('Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 7 '%(s,p)+'%')
elif s>2000:
    p = (s*(4/100))
    s = s + p
    print('Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 4 '%(s,p)+'%')