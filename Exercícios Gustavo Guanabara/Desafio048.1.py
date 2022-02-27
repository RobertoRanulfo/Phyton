soma = 0 #acumulador
cont = 0 #contador
for n in range(1, 501, 2):
    if n % 3 ==0:
        cont = cont + 1 # poderia ser cont += 1 não entendi ainda porque
        soma = soma + n # poderia ser soma += c não entendi ainda porque
print('A soma de todos {} os valores solicitados é {}.'.format(cont, soma))

# lembrando que o % mostra só o resto da divisão. Então o resto da divisão de qualquer número por 3 sendo 0
# mostra que ele é divisível por 3
# conceitos de soma e contagem devem ser vistos mais à frente