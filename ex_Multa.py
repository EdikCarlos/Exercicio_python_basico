vel = float(input('Qual foi a velocidade que o carro passou no radar? : '))
multa = (vel - 80) * 7
if vel > 80:
    print('\033[31mMULTADO!!! Você estava acima da velocidade permitida e terá que pagar R${:.2f}.\033[m'.format(multa))
else:
    print('\033[32mPARABÉNS! Continue sendo um bom motorista!\033[m')
print('\033[30mTENHA UM BOM DIA!\033[m')