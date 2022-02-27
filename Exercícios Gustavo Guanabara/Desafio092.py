from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
idade = date.today().year - nascimento
dados['idade'] = idade
dados['carteira de trabalho'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['carteira de trabalho'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = ((dados['contratação'] + 35) - date.today().year) + idade
for k,v in dados.items():
    print(f'- {k} tem valor {v}')



