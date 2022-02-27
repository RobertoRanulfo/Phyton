# NÃO CONSEGUI FAZER

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
# o split transforma cada palavra em um termo
#.strip para desconsiderar os espaços e .upper para transformar tudo em maiúsculas
# o .join une palavras pelo caracter indicado substituindo os espaços pelo caracter
print('Você digitou a frase {}'.format(junto))
inverso = ""
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')

#len mede a quantidade de caracteres