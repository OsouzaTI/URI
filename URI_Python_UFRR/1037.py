intervalos = ['[0,25]','(25,50]','(50,75]','(75,100]']
n = float(input())

if n >= 0 and n <= 25: print('Intervalo '+intervalos[0])
elif n > 25 and n <= 50: print('Intervalo '+intervalos[1])
elif n > 50 and n <= 75: print('Intervalo '+intervalos[2])
elif n > 75 and n <= 100: print('Intervalo '+intervalos[3])
else: print('Fora de intervalo')