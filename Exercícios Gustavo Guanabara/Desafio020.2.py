from random import shuffle
a1 = str(input('Primeiro aluno '))
a2 = str(input('Segundo aluno '))
a3 = str(input('Terceiro aluno '))
a4 = str(input('QUarto aluno '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação é a seguinte: ')
print(lista)
# Vc poderia criar uma variável ordem e colocar a lista com o shuffle, mas nesse caso não é necessário não sei porquê