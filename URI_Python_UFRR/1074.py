n = int(input())
val = []
for i in range(n):
	val.append(int(input()))
for k in range(len(val)):
	if val[k] > 0:
		if val[k]%2==0:
			print('EVEN POSITIVE')
		else:
			print('ODD POSITIVE')
	elif val[k] == 0:
		print('NULL')
	else:
		if val[k]%2==0:
			print('EVEN NEGATIVE')
		else:
			print('ODD NEGATIVE')