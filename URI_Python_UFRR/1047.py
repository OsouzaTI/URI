# -*- coding: utf-8 -*-

i, mi, f, mf = map(int, input().split(' '))
if i==f and mi==mf:print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    if i == f and mf > mi:
        horas = 0
        minutos = mf - mi
        print('O JOGO DUROU %i HORA(S) E %i MINUTO(S)'%(horas,minutos))
    elif i == f and mf < mi:
        horas = 24 - 1
        minutos = 60 - (mi - mf)
        print('O JOGO DUROU %i HORA(S) E %i MINUTO(S)'%(horas,minutos))
    elif i>f and mi < mf :
        horas = abs(i - (f+12) - 12)
        minutos = mf - mi
        print('O JOGO DUROU %i HORA(S) E %i MINUTO(S)'%(horas,minutos))
    elif i>f and mi > mf:
        horas = abs(i - (f+12) - 12) - 1
        minutos = 60 - (mi - mf)
        print('O JOGO DUROU %i HORA(S) E %i MINUTO(S)'%(horas,minutos))
    elif f>i and mi < mf :
        horas = f - i
        minutos = mf - mi
        print('O JOGO DUROU %i HORA(S) E %i MINUTO(S)'%(horas,minutos))
    elif f>i and mi > mf:
        horas = (f - i) - 1
        minutos = 60 - (mi - mf)   
        print('O JOGO DUROU %i HORA(S) E %i MINUTO(S)'%(horas,minutos))