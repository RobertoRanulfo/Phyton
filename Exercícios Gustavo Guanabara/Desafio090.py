aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado'
elif 5 <= aluno['média'] <= 7:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'
for k, v in aluno.items():
    print(f'- {k} é igual a {v}.')

