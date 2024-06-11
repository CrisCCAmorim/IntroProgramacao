# ANJOLINA

qtd_galinheiros=int(input())
animais=[]

for i in range(0,qtd_galinheiros,1):
    novo_galinheiro=input().split(', ')
    animais= animais + novo_galinheiro

qtd_coelhos=animais.count('Coelho')
if qtd_coelhos>0:
    print(f'A fazenda tem {qtd_coelhos} coelhos!')
else:
    print('Poxa que pena, não temos coelhos.')

qtd_galinhas=animais.count('Galinha')
if qtd_galinhas>0:
    print(f'A fazenda tem {qtd_galinhas} galinhas!')
else:
    print('Poxa que pena, não temos galinhas.')

qtd_patos=animais.count('Pato')
if qtd_patos>0:
    print(f'A fazenda tem {qtd_patos} patos!')
else:
    print('Poxa que pena, não temos patos.')


# RICARDO

lista_compras=input().split(', ')

sementes_pierre=input().split(', ')

if 'Melão' in lista_compras:
    print('Eita parece que não estão vendendo melões, ouvi boatos que tem alguém roubando eles. Um tal de Pedro Elias...')

itens_comprados=[]
for item_lista_compras in lista_compras:
    for item_vendido in sementes_pierre:
        if item_lista_compras==item_vendido and item_vendido not in itens_comprados:
            itens_comprados.append(item_vendido)
  

if len(itens_comprados)==0:
    print('Poxa, acho que ficaremos sem plantações.')
elif itens_comprados==lista_compras:
    print('Consegui comprar todas as frutas que queria!')
else:
    print('Consegui comprar as seguintes sementes:')
    itens_comprados.sort()
    for i in range(0,len(itens_comprados)-1,1):
        print(itens_comprados[i],end=', ')
    else:
        print(itens_comprados[-1])


# STEFAN

itens_mochila=input().split(', ')

qtd_itens=input().split(', ')

if ('Barra de ferro' in itens_mochila) and ('Quartzo refinado' in itens_mochila) and ('Asa de morcego' in itens_mochila):
    indx_barra=itens_mochila.index('Barra de ferro')
    qtd_barra=qtd_itens[indx_barra]

    indx_quartzo=itens_mochila.index('Quartzo refinado')
    qtd_quartzo=qtd_itens[indx_quartzo]

    indx_asa=itens_mochila.index('Asa de morcego')
    qtd_asa=qtd_itens[indx_asa]

    qtd_antenas=[int(qtd_barra),int(qtd_quartzo),int(qtd_asa)//5]
    qtd_antenas.sort()
    print(f'Com os itens que tenho, consigo fazer {qtd_antenas[0]} para-raios!')

else:
    print(f'Com os itens que tenho, consigo fazer 0 para-raios!')
