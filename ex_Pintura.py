l = float(input('Qual a largura total da parede a ser pintada? :'))
h = float(input('Qual a altura total da parede a ser pintada? :'))
area = l * h
tinta = area/2
print('A área total do cômodo é de {:.2f}m² e será necessário {:.1f} litros de tinta para pintar tudo!!!'.format(area, tinta))