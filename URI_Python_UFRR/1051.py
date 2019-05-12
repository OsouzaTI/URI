s = float(input())

if s >= 0 and s <= 2000:
    print('Isento')
elif s>= 2000.01 and s <= 3000:
    t = s - 2000
    p = t * 0.08
    print('R$ %.2f'%(p))
elif s>= 3000.01 and s <= 4500:
    t = s - 3000
    p = t * 0.18 + (1000*0.08)
    print('R$ %.2f'%(p))
elif s>4500:
    t = s - 4500
    p = t * 0.28 + (1500 * 0.18) + (1000*0.08)
    print('R$ %.2f'%(p))
