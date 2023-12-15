# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
# retangulo. Calcule e mostre o comprimento da hipotenusa.

import math

a = float(input('Digite o comprimento do cateto oposto: '))
b = float(input('Digite o comprimento do cateto adjacente: '))

c = math.hypot(a, b)

print('A hipotenusa vai medir {:.2f}'.format(c))
