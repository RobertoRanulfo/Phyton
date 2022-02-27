from time import sleep
def maior(*num): # parâmetros empacotados ou seja não há delimitação da qtd de valores
    maior = cont = 0
    print('-=' * 20)
    print('\nAnalisando valores passados...')
    for valor in num:
        print(f'{valor}',end=' ',flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores!')
    print(f'O maior valor informado foi {maior}!')

#Programa principal

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()