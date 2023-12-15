# Faça um conversor de temperatura de ºC para F
c = float(input('Informe a temperatura em ºC: '))

f = ((9 * c) / 5) + 32

print("A temperatura de {:.2f} ºC corresponde a {:.2f}".format(c, f))
