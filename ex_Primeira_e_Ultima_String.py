nome = str(input('Digite seu nome inteiro para obter informações dele: ')).strip().upper()
print('No seu nome a letra A aparece {} vezes.'.format(nome.count('A')))
print('A letra A aparece pela primeira vez na posição {}.'.format(nome.find('A') + 1))
print('A letra A aparece pela ultima vez na posição {}.'.format(nome.rfind('A') + 1 - nome.count(' ')))
