voltas=int(input())
clima=input()
dificuldade=input()
tipo_pneu=input()



if tipo_pneu=='duro':
    durabilidade=90
elif tipo_pneu=='médio':
    durabilidade=70
else:
    durabilidade=50


if clima == 'sol':
    if tipo_pneu == 'chuva':
        durabilidade = durabilidade - (voltas*15)
    elif tipo_pneu == 'macio':
        if dificuldade=='alta':
            durabilidade = durabilidade - (voltas*3)
        else:
            durabilidade = durabilidade - (voltas*2)
    elif tipo_pneu=='duro':
        if dificuldade=='alta':
            durabilidade = durabilidade - voltas
    else:
        if dificuldade!='alta':
           durabilidade = durabilidade - (voltas*2) 

else:
    if tipo_pneu == 'chuva':
        if dificuldade=='alta':
            durabilidade = durabilidade - (voltas*3)
        elif dificuldade=='média':
            durabilidade = durabilidade - (voltas*2)
        else:
            durabilidade = durabilidade - voltas 
    else:
        durabilidade = durabilidade - (voltas*15)

if durabilidade>=20:
    print(f'A Ferrari obteve sucesso!! Dessa vez a equipe escolheu a melhor estratégia! A equipe teve que realizar poucas paradas! Devido o desgaste nos pneus de {durabilidade}.')
else:
    print(f'Não foi dessa vez! A equipe da Ferrari não obteve um bom resultado devido à grande degradação nos pneus de {durabilidade} e uma alta quantidade de paradas, o que acabou permitindo com que a Red Bull saísse na frente.')



# voltas=int(input())
# clima=input()
# dificuldade=input()
# tipo_pneu=input()


# if tipo_pneu=='duro':
#     durabilidade=90
# elif tipo_pneu=='médio':
#     durabilidade=70
# elif tipo_pneu=='macio' or tipo_pneu=='chuva':
#     durabilidade=50

# if clima=='sol' and tipo_pneu=='chuva':
#     durabilidade = durabilidade - (voltas*15)
# elif clima=='chuva' and tipo_pneu!='chuva':
#     durabilidade = durabilidade - (voltas*15)
# elif clima=='sol' and dificuldade!='alta' and (tipo_pneu=='macio' or tipo_pneu=='medio'):
#     durabilidade = durabilidade - (voltas*2)
# elif clima=='sol' and dificuldade=='alta' and tipo_pneu=='macio':
#     durabilidade = durabilidade - (voltas*3)
# elif clima=='sol' and dificuldade=='alta' and tipo_pneu=='duro':
#     durabilidade = durabilidade - voltas
# elif clima=='chuva' and dificuldade=='baixa' and tipo_pneu=='chuva':
#     durabilidade = durabilidade - voltas
# elif clima=='chuva' and dificuldade=='média' and tipo_pneu=='chuva':
#     durabilidade = durabilidade - (voltas*2)
# elif clima=='chuva' and dificuldade=='alta' and tipo_pneu=='chuva':
#     durabilidade = durabilidade - (voltas*3)

# if durabilidade>=20:
#     print(f'A Ferrari obteve sucesso!! Dessa vez a equipe escolheu a melhor estratégia! A equipe teve que realizar poucas paradas! Devido o desgaste nos pneus de {durabilidade}.')
# elif durabilidade<20:
#     print(f'Não foi dessa vez! A equipe da Ferrari não obteve um bom resultado devido à grande degradação nos pneus de {durabilidade} e uma alta quantidade de paradas, o que acabou permitindo com que a Red Bull saísse na frente.')