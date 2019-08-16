menu = input('Escolha a opção: \n'
             '1- Soma de dois números; \n'
             '2- Diferença entre dois numeros; \n'
             '3- Produto entre dois números; \n'
             '4- Divisão entre dois números; \n')

if int(menu) > 0 and int(menu) < 5:
    n1 = input('Digite o primeiro número:')
    n2 = input('Digite o segundo número:')
    if int(menu) == 1:
        print(int(n1) + int(n2))
    elif int(menu) == 2:
        if int(n1) > int(n2):
            print(int(n1) - int(n2))
        else:
            print(int(n2) - int(n1))
    elif int(menu) == 3:
        print(int(n1) * int(n2))

    elif int(menu) == 4:
        if int(n2) == 0:
            print('O denominador não pode ser igual a zero.')
        else:
            print(int(n1) / int(n2))
else:
    print('O número digitado não e valido nesse menu.')