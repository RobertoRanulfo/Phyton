cidade = str(input('Digite a cidade em que você nasceu: ')).strip()
#print('santo' in cidade.lower.strip())
#coocando o .strip depois da variáve ele retira todos os espaços da direita e esquerda
#utilizando o :5 dizemos que ele não tem indicação do começo, então começa a procurar do início
#e termina no código 5, lembrando que começamos a contar do dígiteo 0 e não entra o último
print(cidade[:5].upper() == 'SANTO')

