lados = []

for i in range(0, 3):  # recebe os valores dos lados de um triângulo
    lado = float(input('Digite o lado do triângulo: '))
    if lado <= 0:
        print('O lado de um triângulo não pode ser menor ou igual a zero!')
        break
    else:
        lados.append(lado)


def verificando(*lado):
    if len(lado) == 3:
        if lado[0] > lado[1] + lado[2] or lado[1] > lado[0] + lado[2] or lado[2] > lado[0] + lado[1]:
            return False
        return True


def verificando_o_tipo(*lado):
    if lado[0] == lado[1] == lado[2]:
        return 'É um triângulo equilátero!!'
    elif lado[0] != lado[1] != lado[2] and lado[0] != lado[2]:
        return 'É um triângulo escaleno!!'
    return 'é um triângulo isóceles!!'



if verificando(*lados):
    print(verificando_o_tipo(*lados))
else:
    print('Não é um Triângulo')
