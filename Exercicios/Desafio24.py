# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome santo

cidade = str(input(
    'Digite o nome da cidade para saber se ela começa ou não com o nome de santo: '))

cidade = cidade.title()
teste = 'Santo' in cidade
print(teste)
