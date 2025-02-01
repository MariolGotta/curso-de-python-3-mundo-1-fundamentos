# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salários superiores a R$1250,00 calcule um aumento de 10%.
# Para salários inferiores ou iguais o aumento é de 15%.

salario = int(input('Digite o valor do salário do funcionário: '))

if salario > 1250:
    aumento = 0.1*salario
    final = 1.1*salario
else:
    aumento = 0.15*salario
    final = 1.15*salario
print('O aumento será de {:.2f} e o salário final será de {:.2f}'.format(
    aumento, final))
