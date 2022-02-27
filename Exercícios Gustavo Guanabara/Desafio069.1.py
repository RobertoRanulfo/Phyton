conthomens = 0
contmulheres18 = 0
contidade = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 17:
        contidade += 1
    else:
        contidade += 0
    if sexo == 'M':
        conthomens += 1
    else:
        conthomens += 0
    print('-'* 30)
    if sexo =='M' and idade < 20:
        contmulheres18 += 1
    else:
        contmulheres18 += 0
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {contidade}.')
print(f'Ao todo temos {conthomens} homens cadastrados.')
print(f'E temos {contmulheres18} mulheres com menos de 20 anos.')
