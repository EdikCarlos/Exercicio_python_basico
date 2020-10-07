import math
x = float(input('Digite um ângulo para saber seu Seno, Cosseno e Tangente: '))
sen = math.sin(math.radians(x))
cos = math.cos(math.radians(x))
tg = math.tan(math.radians(x))
print ('O ângulo {} tem o seno {:.2f} o cosseno {:.2f} e a tangente {:.2f}'.format(x, sen, cos, tg))
