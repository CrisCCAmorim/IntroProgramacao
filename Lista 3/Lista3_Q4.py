agricultura=input().split(' - ')
criacao_animais=input().split(' - ')
pesca=input().split(' - ')
mineracao=input().split(' - ')
print('Itens selecionados! Hora de iniciar a mesclagem... Simbora!')

indx_agricultura=int(input())
indx_criacao_animais=int(input())
indx_pesca=int(input())
indx_mineracao=int(input())
print('Combinando Itens...')

print(f'Item para agricultura: {agricultura[indx_agricultura]}')
print(f'Item para criação: {criacao_animais[indx_criacao_animais]}')
print(f'Item para pesca: {pesca[indx_pesca]}')
print(f'Item para mineração: {mineracao[indx_mineracao]}')

mensagem=''
decisao=''
while mensagem!='Gostei de ver! Ir atrás desses itens vai me render boas horas de diversão...' and decisao!='Essa máquina deve estar com defeito...':
    mensagem=input()
    if mensagem=='Esses itens são bem paia, acho que não gostei muito :(':
        decisao=input()
        if decisao=='Bom, vamos tentar mais uma vez...':
            indx_agricultura=int(input())
            indx_criacao_animais=int(input())
            indx_pesca=int(input())
            indx_mineracao=int(input())
            print('Combinando Itens...')

            print(f'Item para agricultura: {agricultura[indx_agricultura]}')
            print(f'Item para criação: {criacao_animais[indx_criacao_animais]}')
            print(f'Item para pesca: {pesca[indx_pesca]}')
            print(f'Item para mineração: {mineracao[indx_mineracao]}')
        elif decisao=='Essa máquina deve estar com defeito...':
            print('É... acho que já chega de Stardew por hoje...')
    elif mensagem=='Gostei de ver! Ir atrás desses itens vai me render boas horas de diversão...':
        print('Meu dia tá garantido, obrigado pela ajuda Pega Móvel!')