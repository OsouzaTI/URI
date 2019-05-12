# -*- coding: utf-8 -*-

p =  input()
p1 = input()
p2 = input()
if p == 'vertebrado':
    if p1 == 'ave':
        if p2 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if p2 == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if p1 == 'inseto':
        if p2 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if p2 == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')