# -*- coding: utf-8 -*-
n = float(input())

print('NOTAS:')

count, t, val = 0, 0, 0
while(t <= n-100):
	count = count + 1
	t = count * 100
print('{} nota(s) de R$ 100.00'.format(count))
val = n - t

count, t = 0, 0
while(t <= val-50):
	count = count + 1
	t = count * 50
print('{} nota(s) de R$ 50.00'.format(count)) 
val = val - t

count, t = 0, 0
while(t <= val-20):
	count = count + 1
	t = count * 20
print('{} nota(s) de R$ 20.00'.format(count)) 
val = val - t

count, t = 0, 0
while(t <= val-10):
	count = count + 1
	t = count * 10
print('{} nota(s) de R$ 10.00'.format(count)) 
val = val - t

count, t = 0, 0
while(t <= val-5):
	count = count + 1
	t = count * 5
print('{} nota(s) de R$ 5.00'.format(count)) 
val = val - t

count, t = 0, 0
while(t <= val-2):
	count = count + 1
	t = count * 2
print('{} nota(s) de R$ 2.00'.format(count)) 
val = val - t

print('MOEDAS:')

count, t = 0, 0
while(t <= val-1):
	count = count + 1
	t = count * 1
print('{} moeda(s) de R$ 1.00'.format(count)) 
val = val - t

count, t = 0, 0
while(t <= val-0.50):
	count = count + 1
	t = count * 0.50
print('{} moeda(s) de R$ 0.50'.format(count)) 
val = val - t

count, t = 0, 0
while(t <= val-0.25):
	count = count + 1
	t = count * 0.25
print('{} moeda(s) de R$ 0.25'.format(count)) 
val = val - t

count, t = 0, 0
while(t <= val-0.10):
	count = count + 1
	t = count * 0.10
print('{} moeda(s) de R$ 0.10'.format(count)) 
val = val - t

count, t = 0, 0
while(t <= val-0.05):
	count = count + 1
	t = count * 0.05
print('{} moeda(s) de R$ 0.05'.format(count)) 
val = val - t

#print('{}'.format(val))
count, t = 0, 0
while(t <= val-0.00998):
	count = count + 1
	t = count * 0.00998
print('{} moeda(s) de R$ 0.01'.format(count)) 
val = val - t