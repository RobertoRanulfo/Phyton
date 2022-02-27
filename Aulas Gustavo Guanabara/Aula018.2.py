teste = []
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #Nesse caso estão sendo copiados os elementos da lista como a esquerda e a direira dos
print(teste)            #dois pontos não tem nada, ele puxa do primeiro elemento ao último
print(galera)
teste[0] = 'Maria'
teste[1] = 22
print(teste)
galera.append(teste[:])
print(galera)
