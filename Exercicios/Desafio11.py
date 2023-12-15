# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessário para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

x = float(input('Digite a altura da parede: '))
y = float(input('Digite a largura da parede: '))

area = x * y
qtdade = area / 2

print('A área da parede é de {: .3f} m² e vai ser usado {: .3f} litros de tinta'.format(area, qtdade))
