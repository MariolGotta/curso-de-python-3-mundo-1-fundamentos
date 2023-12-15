# Crie um programa que leia um número real na tela e mostre a sua porção inteira.
# Ex, digite o numero 6.127. R: O numero 6.127 tem a parte inteira 6.

import math

num = float(input('Digite um valor: '))
arred = math.trunc(num)
print('O numero {} tem a parte inteira {}'.format(num, arred))
