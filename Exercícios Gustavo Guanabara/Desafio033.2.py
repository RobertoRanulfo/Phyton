a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
# verificando menor valor. Não se prenda no nome da variável 'menor' poderia ser qualquer outro nome qualquer

me = a
if b < a and b < c:
    menor = b
if c < a and c< b:
    menor = c
print('O menor valor digitado é {}!'.format(me))
# usamos a condicional apenas na variável sem o print inicialmente dizendo que se condição se fizer a variável muda
# no caso a variável era igual a 'a', mas se fizer a condição ela pode ser igual a outra coisa (no caso outra variável)
ma = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado é {}!'.format(ma))
