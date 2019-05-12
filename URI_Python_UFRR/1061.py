dia1 = input().split()
h1, m1, s1 = map(int, input().split(':'))
dia2 = input().split()
h2, m2, s2 = map(int, input().split(':'))
d1 = int(dia1[1])
d2 = int(dia2[1])
#dias
dias = d2 - d1
if h1 > h2:dias -= 1
elif h1 == h2 and m1 > m2:dias -= 1

if dias == -1: dias = 0
#horas
if h1 == h2 and m2 > m1:
    horas = 0
    minutos = m2 - m1
elif h1 == h2 and m2 < m1:
    horas = 24 - 1
    minutos = 60 - (m1 - m2)
elif h1 == h2 and m1 == m2:
    horas = 0
    minutos = 0
elif h1 > h2 and m1 < m2:
    horas = abs(h1 - (h2+12) - 12)
    minutos = m2 - m1
elif h1 > h2 and m1 > m2:
    horas = abs(h1 - (h2+12) - 12) - 1
    minutos = 60 - (m1 - m2)
elif h1 > h2 and m1 == m2:
    horas = abs(h1 - (h2+12) - 12) - 1
    minutos = 0
elif h2 > h1 and m1 < m2:
    horas = h2 - h1
    minutos = m2 - m1
elif h2 > h1 and m1 > m2:
    horas = (h2 - h1) - 1
    minutos = 60 - (m1 - m2)
elif h2 > h1 and m1 == m2:
    horas = (h2 - h1)-1
    minutos = 60 - (m1 - m2)
if minutos == 60:
    horas += 1
    minutos = 0
#segundos
if s1 == s2:
    segundos = 0
elif s1 > s2:
    minutos = minutos - 1
    segundos = 60 - (s1 - s2)
elif s1 < s2:
    segundos = s2 - s1
print('%i dia(s)'%dias)
print('%i hora(s)'%horas)
print('%i minuto(s)'%minutos)
print('%i segundo(s)'%segundos)
