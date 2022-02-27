from datetime import date
atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = atual - ano
print('Quem nasceu em {} tem ou fará {} anos em {}.'.format(ano, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('Ainda faltam {} anos para seu alistamento'.format(18-idade))
    print('Seu alistamento será em {}.'.format(atual+(18-idade)))
else:
    print('Você já deveria ter se alistado há {} anos.'.format(idade-18))
    print('Seu alistamento foi em {}.'.format(atual-(idade-18)))

# aqui importamos a bibioteca datetime e puxamos a fórmula date.today() para saber o dia atual
# incrementamos a date.today(), fazendo date.today().year para retornar apenas o ano atual

