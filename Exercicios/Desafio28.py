# Escreva um programa que faça o computador pensar em um numero entre 0 e 5 e peça para o usuário tentar descobrir qual foi
# o numero escolhido pelo computador
# O usuário deverá escrever na tela se o usuário venceu ou perdeu

import random
from time import sleep

n = int(input('Digite um número entre 0 e 5 e veja se é o mesmo que o computador escolheu: '))

n1 = random.randrange(0, 5, 1)
tentativa = 0
print ('Processando...')

sleep(3)

while tentativa < 6:

    if n == n1:
        print('Você acertou!!')
        break

    else:
        tentativa += 1
        n = int(input('Você errou \n'+'Digite outro número entre 0 e 5 e veja se agora você acerta: '))

print('O número escolhido foi: ', n1)
