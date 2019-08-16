numero = int(input('Digite um número:'))
soma = 0
qtd = 0
media = 0
maiorN = numero
menorN = numero
mediaP = 0


while numero != 0:
    soma = soma + numero
    qtd = qtd + 1

    if maiorN < numero:
        maiorN = numero
    if menorN > numero:
        menorN = numero
    if (numero % 2) == 0:
        mediaP = mediaP + numero
    numero = int(input('Digite um número:'))

print('A soma dos números digitados é', soma)
print('A quantidades de números digitados é', qtd)
print('O maior numero digitado é ', maiorN)
print('O menor numero digitado é ', menorN)
print('A média dos números digitado é ', (soma/qtd))
print('A media dos números pares digitados é', (mediaP/qtd))
