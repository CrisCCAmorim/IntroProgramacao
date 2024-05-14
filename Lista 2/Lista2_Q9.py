print('Bem vindo ao jogo da forca do ye!')

num_musicas = int(input())
musicas_certas=0

for i in range (1,num_musicas+1,1):
    musica=input()
    
    #calculando o numero de tentativas e criando a forca
    tentativas=0
    forca=''
    for caracter in musica:
        if caracter!=' ':
            tentativas+=1
            forca = forca+'_'
        else:
            forca = forca+' '
    tentativas=tentativas*2

    #imprimindo qual o numero da musica
    if i<num_musicas:
        print(f'Esta é a música {i} de {num_musicas}.')
    else:
        print('Última música!')

    #iniciando a forca
    tem_letra= False
    tinha_letra= False
    while forca!=musica and tentativas>0:
        letra=input()
        
        for i in range (0,len(musica),1):
            if letra==musica[i]:
                tem_letra=True
                if letra!=forca[i]:
                    forca=forca[:i]+letra+forca[i+1:]
                else:
                    tinha_letra=True

        
        if tem_letra==True:
            if tinha_letra==False: 
                print('Uhuuuuu! Consegui adivinhar uma letra!')
                tem_letra=False
                tentativas-=1
            else:
                print('Já tinha colocado essa letra antes, preciso de mais atenção.')
                tinha_letra=False
        else:
            print(f'Eita! Parece que a letra {letra} não está na música secreta!')
            tentativas-=1

        print(f'Resposta atual: {forca}')

#checando se o usuário acertou a música
    if forca==musica:
        print('Isso! Consegui acertar uma música!')
        musicas_certas+=1
    else:
        print(f'Vish, essa tava difícil, a música era {musica}. Espero acertar a próxima!')

print(f'Consegui acertar {musicas_certas} músicas de {num_musicas}!')

taxa_acerto=musicas_certas/num_musicas
if taxa_acerto<=0.5:
    print('Poxa, eu conseguiria ter ido bem melhor, vou escutar todos os álbuns em repeat!')
elif taxa_acerto>0.5 and taxa_acerto<=0.75:
    print('Foi um bom resultado, vou começar a escutar mais músicas do Kanye West.')
elif taxa_acerto>0.75 and taxa_acerto<=1:
    print('Eu sou o próprio Kanye West.')