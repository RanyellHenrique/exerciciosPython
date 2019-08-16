numeros = []

for numero in range(0, 8):
    numeros.append(int(input('Digite um número: ')))

soma1 = int(input('Digite a primeira posição para ser somada: '))
soma2 = int(input('Digite a segunda posição para ser somada: '))

soma = numeros[soma1] + numeros[soma2]

print(soma)