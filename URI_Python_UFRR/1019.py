s = int(input())
horas = int(s / 3600)
minutos = int((s % 3600)/60) 
segundos = (s % 3600) % 60
print('{0}:{1}:{2}'.format(horas,minutos,segundos))