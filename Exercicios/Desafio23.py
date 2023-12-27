# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# Ex: 1834
# Unidade 4 , dezena 3, centena 8, milhar 1

numero = str(input('Digite um número: '))

numero = numero.strip()
print('Unidade: ', numero[3])
print('Dezena: ', numero[2])
print('Centena: ', numero[1])
print('Milhar: ', numero[0])
