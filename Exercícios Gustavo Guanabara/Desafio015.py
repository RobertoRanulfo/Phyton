d = int(input('Por quantos dias foi alugado? '))
km = int(input('Quantos quilômetros foram rodados? '))
pkm = 0.15
pd = 60

print('O total a pagar por {} dias alugados e {}km rodados é R${:.2f}!'.format(d, km, (d * pd)+(km * pkm)))


