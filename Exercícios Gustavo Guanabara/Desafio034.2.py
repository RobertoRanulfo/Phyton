salário = float(input('Digite o salário do funcionário: R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('O salário do funcionário que era R${:.2f}, agora é R${:.2f}'.format(salário, novo))
