linha1 = input().split(' ')
a, b, c = map(int, linha1)
if a>=0 or b>=0 or c>=0:
    maiorAB = (a+b+abs(a-b))/2
    maiorAC = (a+c+abs(a-c))/2
    maiorBC = (b+c+abs(b-c))/2
else:
    if a > b: maiorAB = a
    else: maiorAB = b
    if a > c:maiorAC = a
    else:maiorAC = c
    if b > c:maiorBC = b
    else:maiorBC = c
temp = []
if maiorAB == a and maiorAC == a:
    # maior a
    if maiorBC == b:
        print('{}\n{}\n{}'.format(c,b,a))
    else:
        print('{}\n{}\n{}'.format(b,c,a))
elif maiorAB == a and maiorAC == c:
    # maior c
    print('{}\n{}\n{}'.format(b,a,c))
elif maiorAB == b and maiorBC == b:
    # maior b
    if maiorAC == a:
        print('{}\n{}\n{}'.format(c,a,b))

    else:
        print('{}\n{}\n{}'.format(a,c,b))
elif maiorAB == b and maiorBC == c:
    # maior c
    print('{}\n{}\n{}'.format(a,b,c))
print('\n{}\n{}\n{}'.format(a,b,c))