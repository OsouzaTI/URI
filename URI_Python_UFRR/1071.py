x = int(input())
y = int(input())
if x > y:
	temp = y
	y = x
	x = temp

soma_impa = 0
k = 1
j = x
while(j < y-1):
	if (x+k)%2!=0:
		soma_impa += (x+k)
	j += 1
	k += 1
print('%i'%soma_impa)