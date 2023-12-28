# Desenvolva um programa que pergunte a distancia de uma viagem em Km
# Calcule o preço da passagem cobrando R$0,50 por km para viagens de até 200km
# e R$ 0,45 por km para viagens mais longas.

distancia = int(input('Digite a distancia da viagem em km: '))

if distancia <= 200:
    valor = distancia * 0.50
    print('O valor da passagem será de {:.2f}'.format(valor))

else:
    valor = distancia * 0.45
    print('O valor da passagem será de {:.2f}'.format(valor))
