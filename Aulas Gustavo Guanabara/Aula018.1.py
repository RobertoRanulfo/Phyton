teste = list()
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste) #neste caso estamos criando uma ligação entre as duas listas
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(teste)
print(galera) # No caso os elementos não se acumularam porque não foi feita uma cópia dos elementos da lista
              # e sim um elo que espelha a lista... dessa forma ela foi copiada mais uma vez do jeito que estava