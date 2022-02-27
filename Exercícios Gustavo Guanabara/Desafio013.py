funcionário = input('Qual o nome do funcionário? ')
sal = float(input('Qual o salário do funcionário? ' ))
aumento = float(input('Qual o aumento percentual? '))
print('{} ganhava R${:.2f}, com {:.2f}% de aumento, passa a receber R${:.2f}'.format(funcionário, sal, aumento, sal+(sal*(aumento/100))))
# cuidado com os parênteses se esquecer de fechar um pode ter problemas
# o exercício pedia com 15% de aumento seria apenas tirar a variável e colocar diretamente 15