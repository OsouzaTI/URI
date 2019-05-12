i, f = map(int, input().split(' '))
if i==f:print('O JOGO DUROU 24 HORA(S)')
else:
    if i > f:
        print('O JOGO DUROU %i HORA(S)'%( abs(i - (f+12) - 12 )) )
    else:
        print('O JOGO DUROU %i HORA(S)'%( f - i ) )