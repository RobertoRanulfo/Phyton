preço = float(input('Qua é o preço do produto? R$'))
desconto = float(input('Qual é o percentual de desconto desse produto? '))
print('O produto que custava R${:.2f}, na promoção com desconto de {:.2f}% vai custar R${:.2f}'.format(preço, desconto, preço - preço * (desconto/100) ))
