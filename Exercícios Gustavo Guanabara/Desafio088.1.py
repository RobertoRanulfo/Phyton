from random import randint
print('-' * 30)
print('      JOGA NA MEGASENA     ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
lista = list()
jogos =[]
tot = 1
cont = 0
while tot <= quant:
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
    print(f'Os números sorteados foram {jogos}')