k = 1
n_k = 60
print('I=1 J=60')
for i in range(60):
    if n_k!=0:
        if k == 3:
            n_k -= 5
            print('I=%i J=%i'%(i,n_k))
            k = 1
        else:
            k += 1



