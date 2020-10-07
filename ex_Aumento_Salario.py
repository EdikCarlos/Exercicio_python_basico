nome = str(input('Qual o nome do(a) funcionário(a)? '))
si = float(input('Qual o salário inicial do(a) funcionário(a) {}? R$'.format(nome)))
p = si + (si * 15 / 100)
print('O salário inicial do(a) funcionario(a) {} era de {:.2f} e com o aumento de 15% foi para R${:.2f}!'.format(nome, si, p))