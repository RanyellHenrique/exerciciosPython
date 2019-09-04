def arquivo():
    nome = input('Digite o nome do arquivo texto: ')
    caracter = input('Digite um caracter: ')

    try:
        with open(nome, 'r') as texto:
            lista = list(texto.read().lower())
            res = list(filter(lambda letra: letra == caracter, lista))
            print(len(res))
    except FileNotFoundError as e:
        print(e)

arquivo()