itens_desejados=input().split(', ')

itens_fazenda=input().split(', ')

itens_achados=[]

for item_desejado in itens_desejados:
    for item_fazenda in itens_fazenda:
        if item_desejado==item_fazenda:
            itens_achados.append(item_desejado)

if len(itens_achados)>0:
    print('Estes são os itens que já tenho na fazenda:')
    for i in range(0,len(itens_achados),1):
        print(f'{i+1}º item: {itens_achados[i]}')

    if itens_achados==itens_desejados:
        print(f'Perfeito, encontrei todos os {len(itens_achados)} itens aqui na fazenda!')
    else:
        qtd_faltando=len(itens_desejados)-len(itens_achados)
        print(f'Vou precisar adquirir {qtd_faltando} itens antes do festival!')
    print('Estou pronto para o festival de Stardew Valley! Que comece a diversão!')
    
else:
    print(f'Parece que estou precisando fazer mais algumas colheitas! Não encontrei nenhum dos {len(itens_desejados)} itens aqui na fazenda.')

