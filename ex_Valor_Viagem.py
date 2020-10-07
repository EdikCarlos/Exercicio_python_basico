km = float(input('Digite quantos quilômetros sua viagem terá para saber o valor da passagem: '))
if km <= 200:
    km1 = km * 0.50
    print('Sua viagem tem {:.0f}Km e custará R${:.2f}'.format(km, km1))
else:
    km1 = km * 0.45
    print('Sua viagem tem {:.0f}Km e custará R${:.2f}'.format(km, km1))
print('BOA VIAGEM!!!')