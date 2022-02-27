n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1+n2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, média))
if média >= 7:
    print('O aluno está APROVADO!')
elif média >= 5 and média < 7:
    print('O aluno está de RECUPERAÇÃO!')
elif média < 5:
    print('O aluno está REPROVADO!')

# o primeiro elif poderia ser feito assim também: if 7 > média >=5 sem usar o 'and'
# o segundo elif pode ser trocado só por else e não precisaria dizer que ele é menor que 5


