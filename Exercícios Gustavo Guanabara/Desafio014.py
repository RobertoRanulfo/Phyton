c = float(input('Informe a temperatura em °C: '))
f = (9 * c) /5 + 32
print('A temperatura de {:.2f}°C corresponde a {:.2f}°F'.format(c, f))
# nesse caso por causa da ordem de precedência não seria necessário os parênteses