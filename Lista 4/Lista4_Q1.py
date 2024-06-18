def calcula_cp(ataque,defesa,stamina,multiplicador):
    cp_maximo = (ataque * (defesa**0.5) * (stamina**0.5) * (multiplicador**2)) / 10
    return cp_maximo

def desempate(pokemon1,pokemon2):
    if len(pokemon1)>len(pokemon2):
        return pokemon1
    else:
        return pokemon2
    

novo_pokemon=''
pokemons=[]
maior_cp=0
houve_empate=False
while novo_pokemon!='Fim':
    novo_pokemon=input()

    if novo_pokemon!='Fim':

        if novo_pokemon not in pokemons:
            pokemons.append(novo_pokemon)
            ataque=int(input())
            defesa=int(input())
            stamina=int(input())
            multiplicador=float(input())

            cp=calcula_cp(ataque,defesa,stamina,multiplicador)

            if len(pokemons)==1 or cp>maior_cp:
                maior_cp=cp
                maior_pokemon=novo_pokemon
            elif cp==maior_cp:
                maior_pokemon=desempate(novo_pokemon,maior_pokemon)
                houve_empate=True

            print('Pokémon computado com sucesso.')
            
        else:
            print('Opa, esse Pokémon já foi analisado.')

if houve_empate==False:
    print(f'O Pokémon com o maior CP na região de Kanto é: {maior_pokemon}, com CP máximo de {maior_cp:.2f}')
else:
    print(f'Foi uma análise difícil, mas o Pokémon vencedor com maior CP é: {maior_pokemon}, com CP máximo de {maior_cp:.2f}')