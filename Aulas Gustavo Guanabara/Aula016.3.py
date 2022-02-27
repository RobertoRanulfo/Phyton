lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim')
print('Forma1')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('------')
print('Forma 2')
for comida in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[comida]} na posição {comida}')
print('------')
print('Forma 3')
for pos,comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

