n=''

segundo_turno=True
turno=1

while segundo_turno==True:
    contagem_total=0
    contagem_kanye=0
    n=''
    while n!='FIM' and contagem_total<300:
        n=input()
        if n!='FIM':
            n=int(n)
            if n%7==0 and n%2!=0:
                contagem_kanye+=20
                contagem_total+=20
            elif n%2==0 and n%7!=0:
                contagem_kanye+=10
                contagem_total+=10
            elif n%2!=0 and n%7!=0:
                contagem_total+=14
        print(f'Contagem Kanye:{contagem_kanye}\nContagem total:{contagem_total}')
    if turno==1:
        if contagem_kanye>170:
            print('O Kanye West conseguiu! Se tornou o próximo presidente dos Estados Unidos e realizou o sonho da sua carreira.')
            segundo_turno=False
        elif contagem_kanye<130:
            print('Caramba, não foi dessa vez pro Kanye, voltaremos mais fortes na próxima.')
            segundo_turno=False
        elif contagem_kanye>=130 and contagem_kanye<=170:
            print('A eleição está disputada, vamos ter um segundo turno!')
            turno=2

    else:
        if contagem_kanye>170:
            print('Depois de um pleito muito acirrado, O Kanye West conseguiu! Se tornou o próximo presidente dos Estados Unidos e realizou o sonho da sua carreira.')
        else:
            print('Caramba, foi uma disputa muito acirrada, mas não foi dessa vez pro Kanye, voltaremos mais fortes na próxima.')
        segundo_turno=False

    print(f'Kanye conseguiu ao final da campanha um total de {contagem_kanye*1000000} votos.')
