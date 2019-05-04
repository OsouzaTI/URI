linha1 = input().split(" ")

a, b, c = linha1

maiorAB = (int(a)+int(b)+abs(int(a)-int(b)))/2
if maiorAB == int(a):
	if int(a) > int(c):
		print('{} eh o maior'.format(int(a)))
	else: print('{} eh o maior'.format(int(c)))

else:
	if int(b) > int(c):
		print('{} eh o maior'.format(int(b) ))
	else: print('{} eh o maior'.format(int(c) ))