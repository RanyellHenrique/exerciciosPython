def arquivos():
    arquivo = input('Digite um nome de arquivo: ')

    try:
        with open(arquivo, 'r') as texto:
           print(len(texto.readlines()))
    except FileNotFoundError as e:
        print('Erro de ', e)

arquivos()