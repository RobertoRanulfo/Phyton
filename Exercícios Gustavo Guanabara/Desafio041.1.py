from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year-ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    classe = 'MIRIM'
    print('Classificação: {}'.format(classe))
elif 14 >= idade > 9:
    classe = 'INFANTIL'
    print('Classificação: {}'.format(classe))
elif 19 > idade >= 14:
    classe = 'JUNIOR'
    print('Classificação: {}'.format(classe))
elif 25 > idade >= 19:
    classe = 'SÊNIOR'
    print('Classificação: {}'.format(classe))
elif idade >= 25:
    classe = 'MASTER'
    print('Classificação: {}'.format(classe))

# fiz diferente do desafio pela questão eu entendi que por exemplo: com 19 anos ele não é mais Junior


#o atleta tem 7 anos
#classificação MIRIM