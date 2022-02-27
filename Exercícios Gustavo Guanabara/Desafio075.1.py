números = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores {números}')
print(f'O valor 9 apareceu {números.count(9)}')
if 3 in números:
    print(f'O número 3 apareceu na posição {números.index(3+1)}')
else:
    print(f'O número 3 não aparece nenhuma vez')
print(f'Os valores pares digitados foram ',end='')
for n in números:
    if n % 2 ==0:
        print(n, end=' ')


