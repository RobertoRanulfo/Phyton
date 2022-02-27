casa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual o salário do comprardor? R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação= casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(casa, anos, prestação))
if prestação < salário * 30/100:
    print('Seu empréstimo foi aprovado!')
else:
    print('Seu empréstimo não pode ser concedido.')

#Para pagar uma casa de x reais em tantos anos a prestação será de x reais
#empréstimo concedido ou não