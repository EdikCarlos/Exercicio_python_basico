from math import hypot
co = float(input('Qual o valor do cateto oposto do triângulo?: '))
ca = float(input('Qual o valor do cateto adjacente do triângulo?: '))
h = hypot(co, ca)
print('A hipotenusa desse trianqulo será {:.2f}'.format(h))

