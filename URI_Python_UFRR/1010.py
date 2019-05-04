linha1 = input().split(" ")
linha2 = input().split(" ")

cp, qp, vp = linha1
cn, qn, vn = linha1
total = ( int(qp)*float(vp) ) + ( int(qn) * float(vn) )
print('VALOR A PAGAR: R$ {0:.2f}'.format(total))
