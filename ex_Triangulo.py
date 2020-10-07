l1 = float(input('Digite a primeira medida: '))
l2 = float(input('Digite a segunda medida: '))
l3 = float(input('Digite a terceira medida: '))
if (l2 - l3) < l1 < l2 + l3 and (l1 - l3) < l2 < l1 + l3 and (l1 - l2) < l3 < l1 + l2:
    print('\033[32mÉ POSSIVEL FAZER UM TRIÂNGULO COM ESSAS MEDIDAS!!!\033[m')
else:
    print('\033[31mNÃO É POSSÍVEL FAZER UM TRIÂNGULO COM ESSAS MEDIAS!\033[m')