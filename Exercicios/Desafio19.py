# Um professor quer sortear um de seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome
# do escolhido.

import random

primeiro = str(input('Digite o nome do primeiro aluno: '))
segundo = str(input('Digite o nome do segundo aluno: '))
terceiro = str(input('Digite o nome do terceiro aluno: '))
quatro = str(input('Digite o nome do quarto aluno: '))

lista = [primeiro, segundo, terceiro, quatro]

sorteado = random.choice(lista)

print('O aluno escolhido foi: {}'.format(sorteado))
