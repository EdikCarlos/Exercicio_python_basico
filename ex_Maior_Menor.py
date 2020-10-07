n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n2 < n1 > n3 and n1 > n2 < n3:
    print('O maior número é {} e o menor número é {}.'.format(n1, n2))
if n1 < n3 > n2 and n3 > n2 < n1:
    print('O maior número é {} e o menor número é {}.'.format(n3, n2))
if n3 < n1 > n2 and n2 > n3 < n1:
    print('O maior número é {} e o menor número é {}.'.format(n1, n3))
if n1 < n3 > n2 and n2 > n1 < n3:
    print('O maior número é {} e o menor número é {}.'.format(n3, n1))
if n1 < n2 > n3 and n2 > n1 < n3:
    print('O maior número é {} e o menor número é {}.'.format(n2, n1))
if n1 < n2 > n3 and n2 > n3 < n1:
    print('O maior número é {} e o menor número é {}.'.format(n2, n3))
