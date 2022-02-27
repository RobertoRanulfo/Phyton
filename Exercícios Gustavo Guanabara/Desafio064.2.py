n = 0
soma = 0
cont = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
   cont +=1
   soma = soma + n # soma += n
   n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, soma))