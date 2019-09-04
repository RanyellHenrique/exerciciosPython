def funcao():
    try:
        with open('arq.txt', 'w') as arquivo:
            while True:
                texto = input('Digite um texto ou "0" para sair: ')
                if texto != '0':
                    arquivo.write(texto + '\n')
                else:
                    break
    except:
        print('Ocorreu um erro')


funcao()
