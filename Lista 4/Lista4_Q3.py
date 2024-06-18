def registra_treinadores(qntd_treinadores):
    nomes_treinadores=[]
    idades_treinadores=[]

    for n in range(qntd_treinadores):
        novo_treinador=input().split(' - ')
        #corrigindo erros de digitação
        novo_treinador[0]=novo_treinador[0].lower()
        novo_treinador[0]=novo_treinador[0].capitalize()

        nomes_treinadores.append(novo_treinador[0])
        idades_treinadores.append(int(novo_treinador[1]))

    lista_treinadores=[nomes_treinadores,idades_treinadores]
    return lista_treinadores

def calculo_eevee(nome,idade):
    nome=nome.lower()
    soma_nome=0
    for letra in nome:
        if letra == 'a':
            soma_nome += 1
        elif letra == 'b':
            soma_nome += 2
        elif letra == 'c':
            soma_nome += 3
        elif letra == 'd':
            soma_nome += 4
        elif letra == 'e':
            soma_nome += 5
        elif letra == 'f':
            soma_nome += 6
        elif letra == 'g':
            soma_nome += 7
        elif letra == 'h':
            soma_nome += 8
        elif letra == 'i':
            soma_nome += 9
        elif letra == 'j':
            soma_nome += 10
        elif letra == 'k':
            soma_nome += 11
        elif letra == 'l':
            soma_nome += 12
        elif letra == 'm':
            soma_nome += 13
        elif letra == 'n':
            soma_nome += 14
        elif letra == 'o':
            soma_nome += 15
        elif letra == 'p':
            soma_nome += 16
        elif letra == 'q':
            soma_nome += 17
        elif letra == 'r':
            soma_nome += 18
        elif letra == 's':
            soma_nome += 19
        elif letra == 't':
            soma_nome += 20
        elif letra == 'u':
            soma_nome += 21
        elif letra == 'v':
            soma_nome += 22
        elif letra == 'w':
            soma_nome += 23
        elif letra == 'x':
            soma_nome += 24
        elif letra == 'y':
            soma_nome += 25
        elif letra == 'z':
            soma_nome += 26

    index=(soma_nome*idade)%8

    return index

agua=['Misty', 'Gary', 'Ivy', 'Blanche']
eletrico=['Ash', 'Ritchie', 'Surge', 'Spark']
fogo=['May', 'Blaine', 'Candela']
psiquico=['Agatha', 'Sabrina', 'Fantina']
sombrio=['Jessie', 'James', 'Giovanni']
gelo=['Lorelei', 'Dawn']
planta=['Max', 'Erika', 'Tracey', 'Mallow']
fada=['Whitney']
nomes_reservados= agua+eletrico+fogo+psiquico+sombrio+gelo+planta+fada

qntd_treinadores=int(input())
treinadores=registra_treinadores(qntd_treinadores)
nomes_treinadores=treinadores[0]
idades_treinadores=treinadores[1]
index_treinadores=[]

for n in range(qntd_treinadores):

    if nomes_treinadores[n] in nomes_reservados:
        if nomes_treinadores[n] in agua:
            print(f'A evolução do Eevee de {nomes_treinadores[n]} é para Vaporeon, o mestre das águas!')
        elif nomes_treinadores[n] in eletrico:
            print(f'O Eevee de {nomes_treinadores[n]} evoluiu para Jolteon, cheio de energia elétrica!')
        elif nomes_treinadores[n] in fogo:
            print(f'O Eevee de {nomes_treinadores[n]} se transformou em Flareon, dominando o calor do fogo!')
        elif nomes_treinadores[n] in psiquico:
            print(f'Espeon é a evolução do Eevee de {nomes_treinadores[n]}, mostrando sua mente brilhante!')
        elif nomes_treinadores[n] in sombrio:
            print(f'A evolução sombria do Eevee de {nomes_treinadores[n]} é Umbreon, deslizando pelas sombras!')
        elif nomes_treinadores[n] in gelo:
            print(f'Glaceon é o novo estágio do Eevee de {nomes_treinadores[n]}, tão frio quanto o gelo!')
        elif nomes_treinadores[n] in planta:
            print(f'O Eevee de {nomes_treinadores[n]} se transformou em Leafeon, um espírito da floresta!')
        elif nomes_treinadores[n] in fada:
            print(f'Sylveon é a evolução mágica do Eevee de {nomes_treinadores[n]}, irradiando bondade e misticismo!')
    else:
        index=calculo_eevee(nomes_treinadores[n],idades_treinadores[n])
        if index==0:
            print(f'A evolução do Eevee de {nomes_treinadores[n]} é para Vaporeon, o mestre das águas!')
        elif index==1:
            print(f'O Eevee de {nomes_treinadores[n]} evoluiu para Jolteon, cheio de energia elétrica!')
        elif index==2:
            print(f'O Eevee de {nomes_treinadores[n]} se transformou em Flareon, dominando o calor do fogo!')
        elif index==3:
            print(f'Espeon é a evolução do Eevee de {nomes_treinadores[n]}, mostrando sua mente brilhante!')
        elif index==4:
            print(f'A evolução sombria do Eevee de {nomes_treinadores[n]} é Umbreon, deslizando pelas sombras!')
        elif index==5:
            print(f'Glaceon é o novo estágio do Eevee de {nomes_treinadores[n]}, tão frio quanto o gelo!')
        elif index==6:
            print(f'O Eevee de {nomes_treinadores[n]} se transformou em Leafeon, um espírito da floresta!')
        elif index==7:
            print(f'Sylveon é a evolução mágica do Eevee de {nomes_treinadores[n]}, irradiando bondade e misticismo!')
        