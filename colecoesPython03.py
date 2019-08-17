lista = []
somaP = 0
qtdP = 0
somaI = 0
qtdI = 0

for i in range(0, 6):
    lista.append(int(input('Digite um número: ')))
    if lista[i] % 2 == 0:
        somaP += lista[i]
        qtdP += 1
    else:
        somaI += lista[i]
        qtdI += 1

print(f'A soma dos numeros impares é {somaI}')
print(f'A soma dos numeros pares é {somaP}')
print(f'A quantidade de números impares é {qtdI}')
print(f'A quantidade de números pares é {qtdP}')
print(lista)
