soma3 = 0
soma5 = 0

for numero in range(0, 1000, 3):
    soma3 = soma3 + numero

for numero in range(0, 1000, 5):
    soma5 = soma5 + numero
    
print(soma5)
print(soma3)