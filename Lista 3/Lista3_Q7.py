linhas_colunas=input().split(' x ')
linhas=int(linhas_colunas[0])
colunas=int(linhas_colunas[1])

# CRIANDO A BANCADA/MATRIZ COM ZEROS

bancada=[]
for i in range(0,linhas,1):
    linha=[]
    for j in range(0,colunas,1):
        linha.append(0)
    bancada.append(linha)


# POSICIONANDO OS ELEMENTOS NA BANCADA/MATRIZ

qtd_elementos=int(input())

for i in range(0,qtd_elementos,1):
    atratividade_posicao=input().split()
    atratividade=int(atratividade_posicao[0])
    posicao=atratividade_posicao[1].split(',')
    linha_atrativ=int(posicao[0].replace('(',''))
    coluna_atrativ=int(posicao[1].replace(')',''))

    bancada[linha_atrativ][coluna_atrativ]=atratividade

# print('Atual Arranjo:') # TESTE!!!!!!!!
# for linha in bancada:
#     print(*linha)

operacao=''

while operacao!='Fim':
    operacao=input()

    # PERMUTAÇÃO
    if operacao=='Permutar':
        elementos_permutados=input().split()

        posicao_elemento1=elementos_permutados[0].split(',')
        posicao_elemento1=[int(posicao_elemento1[0].replace('(','')),int(posicao_elemento1[1].replace(')',''))]
        elemento1=bancada[posicao_elemento1[0]][posicao_elemento1[1]]

        posicao_elemento2=elementos_permutados[1].split(',')
        posicao_elemento2=[int(posicao_elemento2[0].replace('(','')),int(posicao_elemento2[1].replace(')',''))]
        elemento2=bancada[posicao_elemento2[0]][posicao_elemento2[1]]

        bancada[posicao_elemento1[0]][posicao_elemento1[1]]=elemento2
        bancada[posicao_elemento2[0]][posicao_elemento2[1]]=elemento1
       
        # print('Atual Arranjo:') # TESTE!!!!!!!!
        # for linha in bancada:
        #     print(*linha)

    # TRANSPOSIÇÃO
    if operacao=='Transposição':
        nova_bancada=[]
        for j in range(0,colunas,1):
            linha=[]
            for i in range(0,linhas,1):
                linha.append(bancada[i][j])
            nova_bancada.append(linha)
        bancada=nova_bancada
        linhas=len(bancada)
        colunas=len(bancada[0])

        # print('Atual Arranjo:') # TESTE!!!!!!!!
        # for linha in bancada:
        #     print(*linha)

    # REMOÇÃO
    if operacao=='Remover':
        for i in range(0,linhas,1):
            for j in range(0,colunas,1):
                if i==0 and j==0:
                    if bancada[0][0]>0:
                        item_removido=bancada[0][0]
                    else:
                        item_removido=100
                elif bancada[i][j]<item_removido and bancada[i][j]>0:
                    item_removido=bancada[i][j]
        for linha in bancada:
            if item_removido in linha:
                indx_item_removido=linha.index(item_removido)
                linha[indx_item_removido]=0
        
        # print('Atual Arranjo:') # TESTE!!!!!!!!
        # for linha in bancada:
        #     print(*linha)

print('Atual Arranjo:')
for linha in bancada:
    print(*linha)

