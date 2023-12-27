# Faça um programa que leia a frase pelo teclado e mostre
# Quantas vezes aparece a letra A
# Em que posição ela aparece na primeira vez
# Em que posição ela aparece na ultima vez

frase = str(input('Digite uma frase para saber quantas vezes aparecem a letra A e em que posição ela está na primeira e na ultima vez: '))

frase = frase.lower()
quantidade = frase.count('a')
print('A letra A aparece', quantidade, 'vezes')

procurar_esq = frase.find('a') + 1
print(procurar_esq)

procurar_dir = frase.rfind('a') + 1
print(procurar_dir)
