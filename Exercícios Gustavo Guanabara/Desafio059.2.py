from time import sleep
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
print('''[ 1 ] Somar
[ 2 ] multiplicar
[ 3 ] saber o maior
[ 4 ] novos números
[ 5 ] sair do programa''')
opção = int(input('>>>>> Qual a sua opção? '))
while opção != 5:
    if opção > 5:
        print('Dados inválidos!')
        print('''
        [ 1 ] Somar
        [ 2 ] multiplicar
        [ 3 ] saber o maior
        [ 4 ] novos números
        [ 5 ] sair do programa''')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
        opção = int(input('>>>>> Qual a sua opção? '))
    else:
        if opção == 1:
            resultado = primeiro + segundo
            print('{} + {} = {}'.format(primeiro, segundo, resultado))
            print('''
            [ 1 ] Somar
            [ 2 ] multiplicar
            [ 3 ] saber o maior
            [ 4 ] novos números
            [ 5 ] sair do programa''')
            opção = int(input('>>>>> Qual a sua opção? '))
        elif opção == 2:
            resultado = primeiro * segundo
            print('{} x {} = {}'.format(primeiro, segundo, resultado))
            print('''
            [ 1 ] Somar
            [ 2 ] multiplicar
            [ 3 ] saber o maior
            [ 4 ] novos números
            [ 5 ] sair do programa''')
            opção = int(input('>>>>> Qual a sua opção? '))
        elif opção == 3:
            if primeiro == segundo:
                print('{} é igual a {}.'.format(primeiro, segundo))
            elif primeiro > segundo:
                print('{} é maior que {}.'.format(primeiro, segundo))
            elif primeiro < segundo:
                print('{} é maior que {}'.format(segundo, primeiro))
            print('''
            [ 1 ] Somar
            [ 2 ] multiplicar
            [ 3 ] saber o maior
            [ 4 ] novos números
            [ 5 ] sair do programa''')
            opção = int(input('>>>>> Qual a sua opção? '))
        elif opção == 4:
            primeiro = int(input('Primeiro número: '))
            segundo = int(input('Segundo número: '))
            print('''
            [ 1 ] Somar
            [ 2 ] multiplicar
            [ 3 ] saber o maior
            [ 4 ] novos números
            [ 5 ] sair do programa''')
            opção = int(input('>>>>> Qual a sua opção? '))
sleep(2)
print('Fim do programa')
