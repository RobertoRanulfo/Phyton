from time import sleep

def contador(início, fim, passo):
    print('-=' * 15)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}.')
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo == 1
    if início < fim:
        cont = início
        while cont <= fim:
            print(f'{cont}',end=' ',flush=True)
            sleep(0.3)
            cont += passo
        print('Fim!')
    else:
        cont = início
        while cont >= fim:
            print(f'{cont}', end=' ',flush=True)
            sleep(0.3)
            cont -= passo
        print('Fim!')




contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 15)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Iníicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
