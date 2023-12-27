# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsuclas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quatas letras tem o primeiro nome


frase = str(input('Digite seu nome completo: '))

frase = frase.strip()

print('Mostrando o nome com todas as letras maiúsculas: ', frase.upper())
print('Mostrando o nome com todas as letras minúculas: ', frase.lower())

quantidade = len(frase) - frase.count(' ')
print('A quantidade total de letras, sem considerar espaços: ', quantidade)

dividido = frase.split()
print('O seu primeiro nome é', dividido[0],
      'e ele tem ', len(dividido[0]), 'letras')
