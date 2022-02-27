galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: ')).upper()[0]
        if pessoa['sexo'] in 'MmFf':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas com S ou N')
    if resp == 'N':
        break
print('-=' *30)
print(galera)
print(f'Ao todo tempos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'A média de idade é de {média:.2f} anos')
print('As mulheres cadastradas foram ',end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}',end='')
print(f'Lista de pessoas que estão acima da média de idade: ')
for p in galera:
    if p['idade'] >= média:
        print('    ', end='')
        for k,v in p.items():
            print(f'{k} = {v};',end='')
print('<< ENCERRADO >>')
