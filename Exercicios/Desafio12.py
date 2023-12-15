# Faça um algoritmo que leia o preço de um protduto e mostre seu novo preço, com 5% de desconto

x = float(input('Digite o preço e receba 5% de desconto: '))

pf = 0.95 * x

print('O valor com desconto é de : {: .3f}'.format(pf))
