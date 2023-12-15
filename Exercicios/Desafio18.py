# Faça um programa que leia um angulo qualquer e mostre na tela
# o valor de seno, cosseno e tangente desse angulo.

import math

angulo = float(input('Digite o valor do angulo: '))

print(
    'O angulo {} tem o SENO de {:.2f}/n O angulo {} tem o COSSENO de {:.2f} O angulo {} tem a TANGENTE de {:.2f}'.format(
        angulo, math.sin(math.radians(angulo)), angulo, math.cos(math.radians(angulo)), angulo,
        math.tan(math.radians(angulo))))
