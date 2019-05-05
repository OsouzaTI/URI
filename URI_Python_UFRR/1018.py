n = int(input())

print(n)

count, t, val = 0, 0, 0
while(t <= n-100):
	count = count + 1
	t = count * 100
print('{} nota(s) de R$ 100,00'.format(count))
val = n - t

count, t = 0, 0
while(t <= val-50):
	count = count + 1
	t = count * 50
print('{} nota(s) de R$ 50,00'.format(count)) 
val = val - t

count, t = 0, 0
while(t <= val-20):
	count = count + 1
	t = count * 20
print('{} nota(s) de R$ 20,00'.format(count)) 
val = val - t

count, t = 0, 0
while(t <= val-10):
	count = count + 1
	t = count * 10
print('{} nota(s) de R$ 10,00'.format(count)) 
val = val - t

count, t = 0, 0
while(t <= val-5):
	count = count + 1
	t = count * 5
print('{} nota(s) de R$ 5,00'.format(count)) 
val = val - t

count, t = 0, 0
while(t <= val-2):
	count = count + 1
	t = count * 2
print('{} nota(s) de R$ 2,00'.format(count)) 
val = val - t

count, t = 0, 0
while(t <= val-1):
	count = count + 1
	t = count * 1
print('{} nota(s) de R$ 1,00'.format(count))

