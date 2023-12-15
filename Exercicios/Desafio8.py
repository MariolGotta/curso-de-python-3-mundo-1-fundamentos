# Escreva um programa que leia um valor em metros e exiba convertido em cm e mm

x = float(input('Digite um valor em metro para ser convertido em cm e mm: '))

a = x * 100
b = x * 1000

print('O valor digitado foi {}, em cm é: {:.0f}. Já em mm é {:.0f}'.format(x, a, b))
