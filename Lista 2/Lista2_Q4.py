qtd_exercicios=int(input())
tipo_treino=''

while tipo_treino!='Fim do Treino':
    tipo_treino=input()
    if tipo_treino!='Fim do Treino':
        print(tipo_treino)
        treinos_finalizados=0
        for i in range (0,qtd_exercicios,1):
            musica=input()
            nota_musica=int(input())
            print(f'{i+1}° música {musica} tocando agora')
            if nota_musica<7:
                print('O padre Marcelo está desanimado, não conseguiu finalizar suas séries')
            else:
                print('O padre Marcelo está inspirado, conseguiu finalizar suas séries!')
                treinos_finalizados+=1
        if treinos_finalizados>=qtd_exercicios/2:
            print('ME DEI BEM COM ESSA PLAYLIST, APROVADO')
        else:
            print('NÃO FOI EFETIVO, VOU VOLTAR PARA MINHA PLAYLIST GOSPEL')
