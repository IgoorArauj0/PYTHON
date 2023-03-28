'''
ca = float(input("Digite o valor de Cateto Adjacente: "))
co = float(input("Digite o valor de Cateto Oposto: "))
hi = (ca**2 + co**2) **(1/2)
print ('O Cateto Adjacente é {}, o Cateto Oposto é {}. E o valor da hipotenusa é {:.2f}!'.format(ca,co,hi)) '''

import math
ca = float(input("Digite o valor de Cateto Adjacente: "))
co = float(input("Digite o valor de Cateto Oposto: "))
hi = math.hypot(co,ca)
print ('O Cateto Adjacente é {}, o Cateto Oposto é {}. E o valor da hipotenusa é {:.2f}!'.format(ca,co,hi))

#Ler cateto oposto, cateto adjacente e calcular o valor da hipotenusa.