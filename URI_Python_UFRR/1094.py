n = int(input())
r = 0
s = 0
c = 0
for i in range(n):
    k = input().split(' ')
    if k[1] == 'R':
        r += int(k[0])
    elif k[1] == 'S':
        s += int(k[0])
    else:
        c += int(k[0])

print('Total: %i cobaias'%(r+s+c))
print('Total de coelhos: %i'%c)
print('Total de ratos: %i'%r)
print('Total de sapos: %i'%s)

print("Percentual de coelhos: %.2f"%( c/(r+s+c)*100 )+' %' )
print("Percentual de ratos: %.2f"%(r/(r+s+c)*100)+' %' )
print("Percentual de sapos: %.2f"%(s/(r+s+c)*100)+' %' )

