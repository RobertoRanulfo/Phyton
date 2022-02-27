m1 = input('Tente fugir do comedor de almas para isso escolha as direções com cuidado. ESCOLHA!! direita ou esquerda? ').strip()
if m1.upper() == 'DIREITA':
    print('Você foi bem pirralho...! ')
    m2 = input('e agora? Direita ou esquerda? ')
    if m2.upper() == 'ESQUERDA':
        print('ohhhhh não!!! você conseguiu fugir. Você é o grande vencedor!!')
    elif m2.upper() =='DIREITA':
        print('Seu bastardo... caiu na minha armadinha...está morto!!')
    else:
        print('Você está brincando comigo... deveria ter escolhido uma direção... agora comece tudo de novo!!')
elif m1.upper()=='ESQUERDA':
    print('Você morreu HAHAHAHA')
else:
    print('Você não seguiu uma diretção comece tudo de novo!!!')

