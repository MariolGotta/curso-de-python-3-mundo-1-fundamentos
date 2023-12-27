# Crie um programa que leia o nome de uma pessoa e diga se ela possui o silva no nome

frase = str(input('Digite o nome para saber se ela possui silva no nome: '))

frase = frase.title()
teste = 'Silva' in frase

print(teste)
