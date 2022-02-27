num = [2, 5, 9, 1]
num[2] = 3
num.append(7) # acrescenta um dado à lista depois do último dado existente
num.sort(reverse=True) #deixa os dados em ordem descrescente
print(num)
num.insert(2, 0) #insere dados de forma que o 0 é o dado a ser inserido e o 2 é a posição
num.pop() #exclui o último dado da lista
num.pop(0) #exclui o primeiro dado da lista
num.remove(5) #busca o valor indicado e exclui ele da lista
if 8 in num: # evita um erro caso se tente excluir um dado que não esteja na lista
    num.remove(8)
else:
    print('Não há nenhum valor 8')
print(num)
print(f'Essa lista tem {len(num)} elementos!') # a função len diz a quantidade de dados da lista
