r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end = '')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 and r1 != r3 and r3 != r2:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('Os segmentos acima NÃO PODE FORMAR UM TRIÂNGULO!')

#utilizamos if dentro de if. primeiro confirmamos a primeira hipótese:
#perceba que sempre que a primeira hipótese for confirmada sempre o print debaixo será escrito,
#independente das hipóteses dentro do if