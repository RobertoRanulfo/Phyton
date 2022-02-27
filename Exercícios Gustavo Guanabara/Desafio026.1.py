frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
# utilizamos +1 porque sabemos que a contagem fica errada porque o Python começa no zero
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
# utilizamos agora o r.find para que ele procurasse iniciando do lado direito
