def calcula_efetividade(meu_tipo,tipo_inimigo):
    if meu_tipo=='fogo':
        if tipo_inimigo=='agua':
            efetividade=0.5
        elif tipo_inimigo=='grama':
            efetividade=2
        else:
            efetividade=1
    elif meu_tipo=='agua':
        if tipo_inimigo=='grama':
            efetividade=0.5
        elif tipo_inimigo=='fogo':
            efetividade=2
        else:
            efetividade=1
    elif meu_tipo=='grama':
        if tipo_inimigo=='fogo':
            efetividade=0.5
        elif tipo_inimigo=='agua':
            efetividade=2
        else:
            efetividade=1
    elif meu_tipo=='normal':
        efetividade=1
    
    return efetividade

def calcula_dano(nivel,poder,defesa_inimigo,poder_ataque,efetividade):
    return int(((((2* nivel) + 10) / 250) * (poder/defesa_inimigo * poder_ataque) + 2) * (efetividade))

def turno(meu_pokemon, pokemon_inimigo):
    
    if int(meu_pokemon[6])>int(pokemon_inimigo[6]):             # SE MEU POKEMON FOR MAIS VELOZ QUE O INIMIGO
        print(f'{meu_pokemon[0]} usou {meu_pokemon[7]}')
        efetividade=calcula_efetividade(meu_pokemon[1],pokemon_inimigo[1])
        if efetividade==0.5:
            print('não foi muito efetivo')
        elif efetividade==2:
            print('foi super efetivo!')
        dano=calcula_dano(int(meu_pokemon[2]),int(meu_pokemon[4]),int(pokemon_inimigo[5]),int(meu_pokemon[8]),efetividade)
        
        pokemon_inimigo[3]-=dano
        if pokemon_inimigo[3]>0:                                # SE A VIDA DO INIMIGO AINDA NÃO ESTIVER ZERADA
            
            print(f'{pokemon_inimigo[0]} usou {pokemon_inimigo[7]}')
            efetividade=calcula_efetividade(pokemon_inimigo[1],meu_pokemon[1])
            if efetividade==0.5:
                print('não foi muito efetivo')
            elif efetividade==2:
                print('foi super efetivo!')
            dano=calcula_dano(int(pokemon_inimigo[2]),int(pokemon_inimigo[4]),int(meu_pokemon[5]),int(pokemon_inimigo[8]),efetividade)
            
            meu_pokemon[3]-=dano
    else:
        print(f'{pokemon_inimigo[0]} usou {pokemon_inimigo[7]}')
        efetividade=calcula_efetividade(pokemon_inimigo[1],meu_pokemon[1])
        if efetividade==0.5:
            print('não foi muito efetivo')
        elif efetividade==2:
            print('foi super efetivo!')
        dano=calcula_dano(int(pokemon_inimigo[2]),int(pokemon_inimigo[4]),int(meu_pokemon[5]),int(pokemon_inimigo[8]),efetividade)
        
        meu_pokemon[3]-=dano
        if meu_pokemon[3]>0:
            print(f'{meu_pokemon[0]} usou {meu_pokemon[7]}')
            efetividade=calcula_efetividade(meu_pokemon[1],pokemon_inimigo[1])
            if efetividade==0.5:
                print('não foi muito efetivo')
            elif efetividade==2:
                print('foi super efetivo!')
            dano=calcula_dano(int(meu_pokemon[2]),int(meu_pokemon[4]),int(pokemon_inimigo[5]),int(meu_pokemon[8]),efetividade)
            
            pokemon_inimigo[3]-=dano
    if meu_pokemon[3]<0:
        meu_pokemon[3]=0
    if pokemon_inimigo[3]<0:
        pokemon_inimigo[3]=0
    



meu_pokemon=input().split(', ')
meu_pokemon[3]=int(meu_pokemon[3])
minha_vida=int(meu_pokemon[3])

print(f'escolho você {meu_pokemon[0]}')
equipe_rocket_derrotada=False

while meu_pokemon[3]>0 and equipe_rocket_derrotada==False:
    inimigo=input()
    pokemon_inimigo=input().split(', ')
    pokemon_inimigo[3]=int(pokemon_inimigo[3])
    vida_inimigo=int(pokemon_inimigo[3])

    if inimigo=='um pokemon selvagem aparece!':
        print('vamo botar pra quebrar!')
        print()
        acao=''
        while meu_pokemon[3]>0 and pokemon_inimigo[3]>0 and acao!='correr':
            acao=input()
            if acao=='atacar':
                turno(meu_pokemon,pokemon_inimigo)
                print(f'HP: {meu_pokemon[3]}/{minha_vida} | HP inimigo: {pokemon_inimigo[3]}/{vida_inimigo}')
                if meu_pokemon[3]==0:
                    print(f'{meu_pokemon[0]} derrotado!')
                    print()
                    print(f'Você perdeu esta batalha, infelizmente não conseguiu salvar o professor.')
                elif pokemon_inimigo[3]==0:
                    print(f'{pokemon_inimigo[0]} derrotado!')
                    print()
            elif acao=='correr':
                print('ufa, consegui meter o pé!')
    elif inimigo=='Equipe Rocket':
        print(f'{meu_pokemon[0]}, bora acabar com a raça desses bandidos e salvar o professor!')
        print()
        while int(meu_pokemon[3])>0 and int(pokemon_inimigo[3])>0:
            acao=input()
            if acao=='atacar':
                turno(meu_pokemon,pokemon_inimigo)
                print(f'HP: {meu_pokemon[3]}/{minha_vida} | HP inimigo: {pokemon_inimigo[3]}/{vida_inimigo}')
            elif acao=='correr':
                print('lascou, eles não largam do meu pé!')
        if meu_pokemon[3]==0:
            print(f'{meu_pokemon[0]} derrotado!')
            print()
            print(f'Você perdeu esta batalha, infelizmente não conseguiu salvar o professor.')
        elif pokemon_inimigo[3]==0:
            equipe_rocket_derrotada=True
            print(f'{pokemon_inimigo[0]} derrotado!')
            print()
            print(f'Ufa, derrotei esses bandidos, consegui resgatar o professor! Está pronto para uma nova jornada {meu_pokemon[0]}?')

