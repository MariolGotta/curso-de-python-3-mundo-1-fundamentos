# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa
# R$60,00 por dia e R$0,15 por km rodado
dias = int(input('Quantos dias o carro foi alugado?: '))
km = float(input('Quantos Km rodados?: '))

aluguel = 60 * dias + (km * 0.15)

print('O total a pagar é de {:.2f}'.format(aluguel))
