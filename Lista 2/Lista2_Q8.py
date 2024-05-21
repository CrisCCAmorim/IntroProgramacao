candidato_01=input()
candidato_02=input()
entrada=''
total_delegados_01 = total_delegados_02 = 0
total_votos_01 = total_votos_02 = 0

if candidato_01=='Kanye West' or candidato_02=='Kanye West':
    while entrada!='FIM':
        entrada=input()
        if entrada!= 'FIM':
            estado,num_delegados=entrada.split(', ')

            votos_cand_01 = 'Taylor Swift roubou as urnas!'
            votos_cand_02 = 'Taylor Swift roubou as urnas!'

            while votos_cand_01=='Taylor Swift roubou as urnas!' or votos_cand_02=='Taylor Swift roubou as urnas!':
                votos_cand_01=input()
                while votos_cand_01=='Taylor Swift roubou as urnas!':
                    print('A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!')
                    votos_cand_01=input()
                
                votos_cand_02=input()
                if votos_cand_02=='Taylor Swift roubou as urnas!':
                    print('A Taylor boicotou o Kanye! HOW COULD BE SO HEARTLESS?!')


            if int(votos_cand_01)>int(votos_cand_02):
                porcentagem=100*int(votos_cand_01)/(int(votos_cand_01)+int(votos_cand_02))
                print(f'{candidato_01} obteve maioria no(a) {estado} com {int(porcentagem)}% dos votos.')
                total_delegados_01+=int(num_delegados)
                total_votos_01+=int(votos_cand_01)
            else:
                porcentagem=100*int(votos_cand_02)/(int(votos_cand_01)+int(votos_cand_02))
                print(f'{candidato_02} obteve maioria no(a) {estado} com {int(porcentagem)}% dos votos.')
                total_delegados_02+=int(num_delegados)
                total_votos_02+=int(votos_cand_02)

        else:
            if total_delegados_01>total_delegados_02:
                print(f'Temos o resultado final! {candidato_01} vence a disputa pela presidência, com o apoio de {total_delegados_01} delegados do colégio eleitoral e {total_votos_01} votos populares.')
                if candidato_01=='Kanye West':
                    print('\"Everybody wanted to know what I would do if I didn\'t win... I Guess We\'ll Never Know.\"')
                else:
                    print('\"Não tem problema, eu obtive o molho!\"')
            else:
                print(f'Temos o resultado final! {candidato_02} vence a disputa pela presidência, com o apoio de {total_delegados_02} delegados do colégio eleitoral e {total_votos_02} votos populares.')
                if candidato_02=='Kanye West':
                    print('\"Everybody wanted to know what I would do if I didn\'t win... I Guess We\'ll Never Know.\"')
                else:
                    print('\"Não tem problema, eu obtive o molho!\"')

else:           
    print('Sem o Ye, sem eleição!')


