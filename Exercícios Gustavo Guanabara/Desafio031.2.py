d = float(input('Digite a distância da viagem: '))
print('Você está prestes a começar uma viagem de {:.2f}km.'.format(d))
if d<=200:
    preço = d * 0.50
    print('O preço da sua passagem será R${:.2f}.'.format(preço))
else:
    preço = d * 0.45
    print('O preço da sua passagem será R${:.2f}.'.format(preço))

# colocamos uma variável dentro de cada condição e ela entrará no print abaixo de cada condição