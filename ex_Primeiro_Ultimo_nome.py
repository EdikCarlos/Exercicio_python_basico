nome = str(input('Digite seu nome completo: ')).strip().upper()
n = nome.split()
print('Prazer em te conhecer, seu primeiro nome é {} e seu ultimo nome é {}.'.format(n[0], n[len(n)-1]))
