nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo!')
elif nome == 'João' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('hummm belo nome feminino, gamei!!!')
else:
    print('Seu nome é bem normal...')
print('Tenha um bom dia, {}!'.format(nome))


# usamos o elif para condições aninhadas, quando queremos dar uma segunda condição ou terceira ou...
# lembrando que nas condicionais quando trabalhamos com str (strings) precisamos usar aspas
# podemos usar o 'in' nas condições para saber se qualquer uma das palavras dentro do parêntese, está na
# resposta da variável
# percebi que usando o 'in' se eu escrever a primeira letra do nome ele já entende que está dentro do dado
# bem estranho inclusive se tiver o 'u' de Juliana já dá certo