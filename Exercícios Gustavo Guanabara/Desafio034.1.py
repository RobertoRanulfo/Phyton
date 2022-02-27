s = float(input('Qual o salário do funcionário? R$'))
n1 = s + (s*10/100)
n2 = s + (s*15/100)
if s > 1250:
    print('O novo salário do funcionário é R${}.'.format(n1))
else:
    print('O novo salário do funcionário é R${}.'.format(n2))




