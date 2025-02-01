# Crie um programa que leia o comprimento de três retas
# e diga ao usuario se elas formam ou não um triângulo

a = int(input('Digite o comprimeiro da primeira reta: '))
b = int(input('Digite o comprimento da segunda reta:'))
c = int(input('Digite o comprimento da terceira reta: '))

if (a+b) > c and (b+c) > a and (a+c) > b:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')
