d = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${:.2f} você pode comprar US${:.2f}'.format(d, d/3.27))
# O :.2 diz que são 2 casas decimais, porém se você não colocar o f (:.2f) indicando que é float
# vai dar erro no script
