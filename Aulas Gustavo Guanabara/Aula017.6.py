a = [2, 4, 7]
b = a # criou-se um elo entre as listas e elas serão sempre iguais o que você alterar em uma altera na outra
print(a)
print(b)
a[0] = 1
print(a)
print(b)
c = a[:] # você apenas copiou todos os itens da lista a para a lista c
print(c)
c[0] = 'x'
print(c)
print(a)