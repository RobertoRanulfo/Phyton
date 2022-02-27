print('{:=^40}'.format('LOJAS GUANABARA'))
p = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual sua opção? '))
if opção == 1:
    total = p - (p*10/100)
    print('Sua compra de R$ {:.2f} vai custar R${:.2f} no final.'.format(p, total))
elif opção == 2:
    total = p - (p*5/100)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(p, total))
elif opção == 3:
    total = p
    print('Sua compra será parcelada em 2 x de R$ {:.2f}, totalizando R$ {:.2f}.'.format(p/2,p))
elif opção == 4:
    juros = p * 20/100
    total = p + juros
    nparcelas = int(input('Quantas parcelas? '))
    parcela = total/ nparcelas
    print('Sua compra será parcelada em {}x de R$ {:.2f} com juros de R$ {:.2f}.'.format(nparcelas, parcela, juros))
    print('Sua compra de R$ {:.2f} custará R$ {:.2f} no final!'.format(p, total))
else:
    print('Opção inválida. Digite uma opção de 1 a 4!')





# Sua compra de R$ ... vai custar ... no final.
# quantas parcelas
# Sua compra será parcelada em 10x de 480 com juros.
# sua compra de ... vai custar ... no final
# não sei explicar como o lojas guanabara ficou centralizado em 40 iguais
# mas e se no número de parcelas ele colocar 2? fica o problema