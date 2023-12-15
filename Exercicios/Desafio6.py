# Crie um algorítimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
x = float(input('Digite um número: '))

a = 2 * x
b = 3 * x
c = x ** 0.5

print('O dobro do número digitado é {}, o seu triplo é {} e a sua raiz quadrada é {:.3f128}'.format(a, b, c))
