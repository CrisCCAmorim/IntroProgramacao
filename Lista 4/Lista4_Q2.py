def adicao(status,valor):
    return status+valor

def subtracao(status,valor):
    return status-valor

def multiplicacao(status,valor):
    return status*valor

def divisao(status,valor):
    return status/valor

def potenciacao(status,valor):
    return status**valor

def radiciacao(status,valor):
    return status**(1/valor)


qntd_operacoes=int(input())
if qntd_operacoes!=-1:
    for i in range(qntd_operacoes):
        acao=input()
        status_pokemon=int(input())
        valor_item=int(input())

        if acao=='Quero deixar meu Pokemon mais forte!':
            nome_operacao='Adição'
            status_final=adicao(status_pokemon,valor_item)
        elif acao=='Deixa eu testar esse cogumelo estranho…':
            nome_operacao='Subtração'
            status_final=subtracao(status_pokemon,valor_item)
        elif acao=='Vou evoluir meu Pokemon!':
            nome_operacao='Multiplicação'
            status_final=multiplicacao(status_pokemon,valor_item)
        elif acao=='Não! Essa comida diminui o ataque…':
            nome_operacao='Divisão'
            status_final=divisao(status_pokemon,valor_item)
        elif acao=='E se eu colocar essa Mega Stone…':
            nome_operacao='Potenciação'
            status_final=potenciacao(status_pokemon,valor_item)
        elif acao=='Essa Mega Stone está estranha...':
            nome_operacao='Radiciação'
            status_final=radiciacao(status_pokemon,valor_item)

        print(f'Ao dar esse item eu esperava uma operação de {nome_operacao} e com isso o status do meu Pokemon de {int(status_pokemon)} foi para {int(status_final)}')

    print('Agora tenho confiança que vou vencer!')
else:
    print('Acho que vou desistir, confio no meu Pokemon sem nenhum item!')