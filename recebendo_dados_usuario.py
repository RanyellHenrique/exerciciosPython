# print("Qual é o seu nome?")
nome = input('Qual o seu nome?')

# print('Seja bem-vindo %s' % nome)
# print('Seja bem-vindo {0}'.format(nome))
print(f'Seja bem-vindo {nome}')

#print("Qual sua idade?")

idade = input('Qual a sua idade?')

# print('O %s tem %s anos'% (nome, idade))
# print('O {0} tem {1} anos'.format(nome, idade))
print(f'O {nome} tem {idade} anos')
print(f'O {nome} nasceu em {2019 - int(idade)}')