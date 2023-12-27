# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ulitmo nome separadamente
# Ex Ana Maria Souza, primeiro ana, ultimo Souza

nome = str(input('Digite o nome para saber o primeiro e ultimo nome: '))

nome = nome.strip()
separado = nome.split()

print(nome)
print('Primeiro nome: ', separado[0])
print('Ultimo nome: ', separado[len(separado) - 1])
