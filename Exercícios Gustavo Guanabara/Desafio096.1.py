def área(larg, comp):
    print(f'A área de um terreno {l:.2f} x {h:.2f} é igual a {l*h:.2f}m²')


print('  Controle de terrenos  ')
print('=-' * 15)
l = float(input('LARGURA (m): '))
h = float(input('COMPRIMENTO (m): '))

área(l,h) # aqui estou dizendo que larg(que é o primeiro parâmetro) é igual a l e comp
          # (que é o segundo parâmetro) é igual a h


