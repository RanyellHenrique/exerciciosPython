kilometros = float(input('Digite a distância percorida (Km): '))
litros = float(input('Digite a quantidade de gasolina consumida no percurso (L):'))


def caulculo_de_consumo(kkilometros, llitros):
    consumo = kkilometros / llitros

    if consumo < 8:
        return 'Venda o carro!!'
    elif 8 <= consumo < 14:
        return 'Econômico!!'
    return 'Super econômico!!'


print(caulculo_de_consumo(kilometros, litros))
