# -*- coding: utf-8 -*-
n = int(input())
err = 1
ddd = [
    (61,71,11,21,32,19,27,31),
    ('Brasilia','Salvador','Sao Paulo','Rio de Janeiro','Juiz de Fora','Campinas','Vitoria','Belo Horizonte')
    ]
for i in range(len(ddd[0])):
    if n == ddd[0][i]:
        print(ddd[1][i])
        err = 0
if(err == 1):
    print('DDD nao cadastrado')