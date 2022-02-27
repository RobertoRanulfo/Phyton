# Podemos utilizar um for como se estivéssemos trabalhando com tuplas
def contador(*num):
    for c in num:
        print(c,end=' ')
    print('FIm')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
print('=-'*15)
def cont(*num):
    for c in num:
        print(f'{c}',end='')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)