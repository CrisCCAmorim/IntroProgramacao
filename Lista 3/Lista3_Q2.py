entrada=''
lista_suspeitos=[]
while entrada!='Já temos nossa lista de suspeitos':
    entrada=input()
    if entrada=='Novo suspeito - altíssima periculosidade':
        nome=input()
        lista_suspeitos.insert(0,nome)
    elif entrada=='Novo suspeito - pouco perigoso':
        nome=input()
        lista_suspeitos.append(nome)
    elif entrada=='Livre de suspeita, pode remover':
        nome=input()
        lista_suspeitos.remove(nome)
    elif entrada=='Sujeito mais perigoso do que pensávamos':
        indx_atual=int(input())
        indx_novo=int(input())
        #trocando os suspeitos de lugar
        nome1=lista_suspeitos[indx_atual]
        nome2=lista_suspeitos[indx_novo]
        lista_suspeitos[indx_novo]=nome1
        lista_suspeitos[indx_atual]=nome2
    elif entrada=='Que estranho, esses dois meliantes… troque-os de lugar':
        nome1=input()
        nome2=input()
        for i in range(0,len(lista_suspeitos),1):
            if lista_suspeitos[i]==nome1:
                lista_suspeitos[i]=nome2
            elif lista_suspeitos[i]==nome2:
                lista_suspeitos[i]=nome1
    elif entrada=='Essa posição não esta de acordo, ele não e tão perigoso assim':
        nome=input()
        lista_suspeitos.remove(nome)
        lista_suspeitos.append(nome)
    elif entrada=='Como a lista esta ficando?':
        tamanho_lista=len(lista_suspeitos)
        for i in range(0,tamanho_lista-1,1):
            print(f'{lista_suspeitos[i]},', end=' ')
        else:
            print(f'{lista_suspeitos[tamanho_lista-1]}')

else:
    print('O resultado final ficou assim:')
    tamanho_lista=len(lista_suspeitos)
    for i in range(0,tamanho_lista-1,1):
        print(f'{lista_suspeitos[i]},', end=' ')
    else:
        print(f'{lista_suspeitos[tamanho_lista-1]}')
