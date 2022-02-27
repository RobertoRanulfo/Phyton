nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
# utilizamos o operador do Python in
# para evitar problemas com espaços usamos o strip
# para evitar problemas com maiúsculas e minúsculas, transformamos todas em maiúsculas ou minúscuas
# no nosso caso todas em maiúsculas com o upper()

