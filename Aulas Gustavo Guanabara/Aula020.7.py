#Desempacotamento
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 3, 8)
soma(1, 2, 3, 4)
soma(0, 1)
