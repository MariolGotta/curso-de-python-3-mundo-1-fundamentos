# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

ano = int(input('Digite o ano e descoubra se ele é bissexto: '))

anob = ano % 4
final00 = ano % 400

if anob == 0 and final00 == 0:
    print('Ano Bissexto')

else:
    print('O ano não é Bissexto')
