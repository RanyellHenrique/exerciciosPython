primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o primeiro número: '))
sinal = input('Digite o simbolo da operação: ')


def operacoes(primeiro_numero, segundo_numero, sinal):
    if sinal == '+':
         return primeiro_numero + segundo_numero
    elif sinal == '-':
        return  primeiro_numero - segundo_numero
    elif sinal == '*':
        return  primeiro_numero * segundo_numero
    elif sinal == '/':
        return  primeiro_numero / segundo_numero
    return 'inválido, pois o simbolo digitado é inválido!!'


print(f'O valor da Operação é {operacoes(primeiro_numero, segundo_numero, sinal)}')