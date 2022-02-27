nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))
#preciso diminuir a medida do len por 1, pois ele diz a quantidade de índices ou dados
#e sempre cairá em um dado a mais do que foi digitado

