from datetime import date
ano = int(input('Qual ano você quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO!'.format(ano))
else:
    print('O ano de {} não é BISSEXTO!'.format(ano))

# temos que dizer se o ano é bissexto. Um ano bissexto tem que ser divisíve por 4
# foi utilizado o comando and pra atribuir uma nova condição e o or para usar o ou
# usamos o != para dizer que é diferente
# usamos a biblioteca datetime para puxar a função date.today e pegar o dia de hoje e acrescenta .year, para
# puxar apenas o ano