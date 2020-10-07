item = float(input('Qual o valor do item que receberá o desconto de 5%? R$'))
p = item - (item * 5 / 100)
print('O valor inicial do produto era de R${:.2f}, com o desconto de 5% ficou em R${:.2f}'.format(item, p))