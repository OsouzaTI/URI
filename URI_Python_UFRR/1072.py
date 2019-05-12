n = int(input())
in_ = 0
out_ = 0
for i in range(n):
	n = int(input())
	if 10 <= n <= 20:in_ +=1
	else:out_ += 1
print('%i in\n%i out'%(in_,out_))