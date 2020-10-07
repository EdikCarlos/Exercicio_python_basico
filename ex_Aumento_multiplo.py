sal = float(input('Qual o valor do salário atual do funcionário?: '))
sal1 = sal + (sal * 10/100)
sal2 = sal + (sal * 15/100)
if sal <= 1250 :
    print('O salário do funcionário terá um aumento de 15%, indo para R${:.2f}.'.format(sal2))
else:
    print('O salário do funcionário terá um aumento de 10%, indo para R${:.2f}.'.format(sal1))