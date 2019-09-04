def arquivos():
    arquivo1 = input('Digite o nome do arquivo texto: ')
    arquivo2 = input('Digite o nome de um aquivo para ser criado: ')

    try:
        with open(arquivo1, 'r') as leitura:
            texto = leitura.read()

        with open(arquivo2, 'x') as escrita:
            escrita.write(texto.upper())

    except FileExistsError as e1:
        print(f'Deu erro {e1}')
    except FileNotFoundError as e2:
        print(f'Deu erro {e2}')

arquivos()