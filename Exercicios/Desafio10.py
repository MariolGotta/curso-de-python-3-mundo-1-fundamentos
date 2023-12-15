# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US 1 = R$ 3,27

x = float(input('Digite um valor em Real para saber quantos Dólares você consegue comprar: '))

a = x / 3.27

print('O valor {:.2f} compra {: .2f} dólares.'.format(x, a))
