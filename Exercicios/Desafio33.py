# Faça um programa que leia três números e mostre qual é o maior
# e qual é o menor

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3 and n2 > n3:
    print('O número {:.0f} é o maior e o {:.0f} é o menor'.format(n1, n3))

if n1 > n2 and n1 > n3 and n3 > n2:
    print('O número {:.0f} é o maior e o {:.0f} é o menor'.format(n1, n2))

if n2 > n1 and n2 > n3 and n3 > n1:
    print('O número {:.0f} é o maior e o {:.0f} é o menor'.format(n2, n1))

if n2 > n1 and n2 > n3 and n1 > n3:
    print('O número {:.0f} é o maior e o {:.0f} é o menor'.format(n2, n3))

if n3 > n1 and n3 > n2 and n1 > n2:
    print('O número {:.0f} é o maior e o {:.0f} é o menor'.format(n3, n2))

if n3 > n1 and n3 > n2 and n2 > n1:
    print('O número {:.0f} é o maior e o {:.0f} é o menor'.format(n3, n1))
