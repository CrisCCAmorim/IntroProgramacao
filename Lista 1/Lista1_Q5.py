frase_01=input()
if frase_01=='Tem uma curva vindo aí, me ajuda!':
    direcao_01=input()

frase_02=input()
if frase_02=='Tem uma curva vindo aí, me ajuda!':
    direcao_02=input()

if frase_01=='TÔ EM ÚLTIMO!':
    print('PISA FUNDO')
elif frase_01=='Esse cara não sai da minha frente...':
    print('Ultrapassa ele agora!')
elif frase_01=='Tem uma curva vindo aí, me ajuda!':
    print('FREIA AGORA E ME DIZ PARA QUE LADO É')
    if direcao_01=='DIREITA':
        print('ENTÃO VIRA LOGO!')
    elif direcao_01=='ESQUERDA':
        print('É SÓ VIRAR!')
    else:
        print('Assim não tem como te ajudar, amiga')
elif frase_01=='MEU PNEU FUROU SOCORRO!':
    print('Amiga, calma! Tem um pit stop na tua frente…')
else:
    print('Eita, não entendi nada…')

if frase_02=='TÔ EM ÚLTIMO!':
    print('PISA FUNDO')
elif frase_02=='Esse cara não sai da minha frente...':
    print('Ultrapassa ele agora!')
elif frase_02=='Tem uma curva vindo aí, me ajuda!':
    print('FREIA AGORA E ME DIZ PARA QUE LADO É')
    if direcao_02=='DIREITA':
        print('ENTÃO VIRA LOGO!')
    elif direcao_02=='ESQUERDA':
        print('É SÓ VIRAR!')
    else:
        print('Assim não tem como te ajudar, amiga')
elif frase_02=='MEU PNEU FUROU SOCORRO!':
    print('Amiga, calma! Tem um pit stop na tua frente…')
else:
    print('Eita, não entendi nada…')


print('LET\'S RIDE!')