# Crie um programa que leia um número inteiro e mostre se ele é par ou impar.

n = int(input('Digite um número para saber se é par ou ímpar: '))

n_par = n % 2

if n_par == 0:
    print('O número é par')

else:
    print('O número é impar')
