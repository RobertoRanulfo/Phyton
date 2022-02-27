sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0] #fatiamento pega apenas o primeiro dado 1ª letra
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(sexo))

