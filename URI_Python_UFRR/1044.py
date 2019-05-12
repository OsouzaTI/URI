linha1 = input().split(' ')
a, b = map(int, linha1)
temp = 0
if a > b:
    temp = b
    b = a
    a = temp
    
if (b%a)==0:print('Sao Multiplos')
else:print('Nao sao Multiplos')
    