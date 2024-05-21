num_rodadas=int(input())
desordem_kanye=0
desordem_taylor=0
vitorias_kanye=0
vitorias_taylor=0
n=0


while n<num_rodadas and desordem_kanye<=5 and desordem_taylor<=5 and vitorias_kanye<3 and vitorias_taylor<3:
    print(f'{n+1}° RODADA')

    pontos_rodada_kanye=0
    musica_kanye=input()
    for i in range (1,4,1):
        avaliacao=input()

        if avaliacao=='boa':
            pontos_rodada_kanye+=2
        elif avaliacao=='média':
            pontos_rodada_kanye+=1
        elif avaliacao=='ruim':
            pontos_rodada_kanye-=3
        else:
            descontentamento=''
            while descontentamento!='ORDEM':
                descontentamento=input()
                if descontentamento!='ORDEM':
                    desordem_kanye+=1

    if desordem_kanye<5:
        pontos_rodada_taylor=0
        musica_taylor=input()
        for i in range (1,4,1):
            avaliacao=input()

            if avaliacao=='boa':
                pontos_rodada_taylor+=2
            elif avaliacao=='média':
                pontos_rodada_taylor+=1
            elif avaliacao=='ruim':
                pontos_rodada_taylor-=3
            else:
                descontentamento=''
                while descontentamento!='ORDEM':
                    descontentamento=input()
                    if descontentamento!='ORDEM':
                        desordem_taylor+=1
        
        if desordem_taylor<5:
            if pontos_rodada_kanye>pontos_rodada_taylor:
                print(f'O(a) vencedor(a) da {n+1}° rodada foi Kanye West')
                vitorias_kanye+=1
            elif pontos_rodada_taylor>pontos_rodada_kanye:
                print(f'O(a) vencedor(a) da {n+1}° rodada foi Taylor Swift')
                vitorias_taylor+=1
            else:
                print(f'Não houve vencedor na {n+1}° rodada')
        
        else:
            print('Os fãs do(a) Taylor Swift causaram tanta desordem que ele(a) perdeu o prêmio!')
            print('O(a) vencedor(a) do Cin Awards é Kanye West, parabéns!')
    else:
        print('Os fãs do(a) Kanye West causaram tanta desordem que ele(a) perdeu o prêmio!')
        print('O(a) vencedor(a) do Cin Awards é Taylor Swift, parabéns!')

    n+=1

if desordem_kanye<5 and desordem_taylor<5:
    if vitorias_kanye>vitorias_taylor:
        print(f'O(a) vencedor(a) do Cin Awards, com um total de {vitorias_kanye} vitórias, é Kanye West, parabéns!')
    elif vitorias_kanye<vitorias_taylor:
        print(f'O(a) vencedor(a) do Cin Awards, com um total de {vitorias_taylor} vitórias, é Taylor Swift, parabéns!')
    else:
        print('Como tivemos um empate, agora todos sabem que vocês são grandes artistas, parabéns!')