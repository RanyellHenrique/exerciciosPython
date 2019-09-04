def arquivos():
    texto = input('Digite o nome de um arquivo: ')
    try:
        with open(texto, 'r') as arquivo:
            lista = arquivo.read()
            lista2 = list(lista.lower())
            res = filter(lambda letra: letra =='á'or letra == 'a' or letra == 'e' or letra == 'i' or letra == 'u' or letra == 'o', lista2)
            resultado = list(res)
            print(resultado)
            print(len(resultado))

    except:
        print('Erro')
arquivos()