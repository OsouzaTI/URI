d1 = input().split(' ')
diainicio = int(d1[1])
hinicio, minicio, sinicio = map(int, input().split(':'))
d2 = input().split(' ')
diafinal = int(d2[1])
hfinal, mfinal, sfinal = map(int, input().split(':'))

dia = diafinal - diainicio
hora = hfinal - hinicio
if(hora < 0):
	hora = 24 + hora
	dia = dia - 1

minuto = mfinal - minicio 
if(minuto < 0):
	minuto = 60 + minuto
	hora = hora - 1
	
segundos = sfinal - sinicio
if(segundos < 0):
	segundos = 60 + segundos
	minuto = minuto - 1

if(dia <= 0):
	dia = 0

print("%d dia(s)" %dia)
print("%d hora(s)" %hora)
print("%d minuto(s)" %minuto)
print("%d segundo(s)" %segundos)