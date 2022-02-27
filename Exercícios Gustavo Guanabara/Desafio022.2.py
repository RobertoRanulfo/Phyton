nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúscuas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome)-nome.count(' ')))
# usamos o len para contar os caracteres e depois tivemos que diminuir pelos espaços vazios
# Para acharmos os espaços vazios usamos um recurso direto da string 'count' e entre aspas
# colocamos um espaço vazio para que ele procure e conte todos os espaços vazios
separa = nome.split()
print('Seu primeiro nome é {} e possui {} letras'.format(separa[0], len(separa[0])))
# para contar os carcteres do primeiro não não foi necessário se preocupar com os espaços vazios
# já que o 'len' foi direto no dado '0'