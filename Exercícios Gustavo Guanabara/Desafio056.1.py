somaidade = 0
contm = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for c in range(1, 5):
    print(5 * '-' ,end=' ')
    print('{}ª Pessoa'.format(c),end=' ')
    print(5 * '-')
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    somaidade += idade
    if c ==1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade >maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é {}.'.format(somaidade/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos!'.format(totmulher))
