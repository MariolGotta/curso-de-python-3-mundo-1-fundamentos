# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapssar 80km/h mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada KM acima do limite

velocidade = int(input('Digite a veolicade do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('O valor da multa será de: {:.2f}'.format(multa))
else:
    print('Não foi excedido o limite de velocidade!')
