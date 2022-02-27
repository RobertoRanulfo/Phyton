frase = ('Curso em vídeo Python       ')
print(frase.count('o'))
# Unindo frase.count e dizendo qual letra você pode contar quantas vezes a letra aparece
print(frase.upper())
# Vai transformar todas as palavras da frase em maiúsculas
print(frase.upper().count('O'))
# nesse caso misturamos a fórmula count com upper, assim ele transformou todas em maiúsculas e fez a contagem da letra O
# Lembrando que maiúsculas e minúsculas são diferenciadas no Python
print(len(frase))
# Len é uma fórmula interna que faz a contagem de caracteres
print(len(frase.strip()))
# o strip retira os espaços vazios da esquerda e direita da frase
# você pode colocar um l(left - esquerda) ou r (right - direita) para tirar os espaços vazios apenas de um dos lados