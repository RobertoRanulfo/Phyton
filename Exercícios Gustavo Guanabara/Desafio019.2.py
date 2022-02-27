from random import choice
n1 = str(input('Qual o primeiro aluno? '))
n2 = str(input('Qual o segundo aluno? '))
n3 = str(input('Qual o terceiro aluno? '))
n4 = str(input('Qual o quarto aluno? '))
n5 = str(input('Qual o quinto aluno? '))
lista = n1, n2, n3, n4, n5
escolhido = choice(lista)
print('O aluno (a) escolhido foi {}, parabéns!'.format(escolhido))
