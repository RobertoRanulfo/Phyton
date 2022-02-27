qtd = int(input('Quantos produtos deseja? '))
if qtd <= 2:
    total = qtd * 87
elif 3 <= qtd <= 4:
    total = qtd * 86
elif 5 <= qtd <= 6:
    total = qtd * 85
elif 7  <= qtd <= 10:
    total = qtd * 84
elif qtd > 10:
    total = qtd * 83
print('O valor total da compra é R$ {:.2f}'.format(total))
