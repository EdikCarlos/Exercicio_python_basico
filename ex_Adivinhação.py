from random import randint
from time import sleep
jogador = int(input('Irei pensar em um número de 0 a 5, qual você acredita que será? :'))
print('\033[35m-=-\033[m' * 8)
print('\033[7:35:40mPROCESSANDO...\033[m')
print('\033[35m-=-\033[m' * 8)
sleep(3)
pc = randint(0,5)
if jogador == pc:
    print('\033[32mPARABÉNS! Você acertou o número que eu estava pensando =D!!!\033[m')
else:
    print('\033[31mVOCÊ ERROU! O número que eu pensei foi {} e você falou {}, passou perto!\033[m'.format(pc, jogador))