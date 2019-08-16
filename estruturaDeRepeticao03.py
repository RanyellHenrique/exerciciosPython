numero = int(input('Digite um número par:'))

if (numero % 2) == 0:
    for n in range(numero, 0, -2):
        print(n)
else:
    print('Valor invalido!!')