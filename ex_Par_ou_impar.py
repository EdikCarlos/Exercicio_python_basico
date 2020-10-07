n = int(input('Digite um número para saber se ele é par ou ímpar: '))
if n % 2 == 0:
    print('O número {} é \033[36mPAR\033[m!!!'.format(n))
else:
    print('O número {} é \033[36mÍMPAR\033[m!!!'.format(n))