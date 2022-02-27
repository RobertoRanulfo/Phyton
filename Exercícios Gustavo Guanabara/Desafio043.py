peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / altura ** 2
print('O seu IMC é de {:.2f}.'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 < imc < 25:
    print('Parabéns!! Você está no peso ideal!')
elif 25 < imc < 30:
    print('Você está com SOBREPESO!')
elif 30 < imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA!')

