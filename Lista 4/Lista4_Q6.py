def cria_boxes(qtd):
    if qtd>0:
        if qtd%30==0:
            num_boxes=int(qtd/30)
        else:
            num_boxes=(qtd//30)+1
    elif qtd==0:
        num_boxes=1
    boxes=[]
    for n in range(num_boxes):
        box_n=[]
        for i in range(5):
            linha=[]
            for j in range(6):
                linha.append(0)
            box_n.append(linha)
        boxes.append(box_n)
    return boxes

def captura(qtd,boxes):
    
    while qtd>0:
        if boxes[len(boxes)-1][4][5]==1:  # BOXES CHEIOS
            # CRIA MAIS UM BOX E ADICIONA A LISTA DE BOXES
            novo_box=[]
            for i in range(5):
                linha=[]
                for j in range(6):
                    linha.append(0)
                novo_box.append(linha)
            boxes.append(novo_box)
        else:
            # PERCORRE A MATRIZ ENQUANDO AINDA HOUVER ITENS PRA SER ADICIONADOS
            n=0
            while n<len(boxes) and qtd>0:
                i=0
                while i<5 and qtd>0:
                    j=0
                    while j<6 and qtd>0:
                        if boxes[n][i][j]==0:
                            boxes[n][i][j]=1
                            qtd-=1
                        j+=1
                    i+=1
                n+=1
    
    return boxes

def remover(qtd,boxes):
    box_vazio=[[0,0,0,0,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0],
               [0,0,0,0,0,0]]
    # PERCORRE A MATRIZ DE TRÁS PRA FRENTE ENQUANTO AINDA HOUVER ITENS PARA SER RETIRADOS
    n=-1
    while n>-len(boxes)-1 and qtd>0:
        i=-1
        while i>-6 and qtd>0:
            j=-1
            while j>-7 and qtd>0:
                if boxes[n][i][j]==1:
                    boxes[n][i][j]=0
                    qtd-=1
                j-=1
            i-=1
        n-=1
    # REMOVE AS MATRIZES VAZIAS
    while len(boxes)>1 and boxes[-1]==box_vazio:
        boxes.pop(-1)

    return boxes


# MAIN
qtd_inicial=int(input())
boxes=cria_boxes(qtd_inicial)
boxes=captura(qtd_inicial,boxes)

comando=''
while comando!='Finalizar':
    comando=input()
    if comando!='Finalizar':
        qtd=int(input())
        if comando=='Capturar':
            boxes=captura(qtd,boxes)
        if comando=='Transferir':
            boxes=remover(qtd,boxes)

        for box_n in range(len(boxes)):
            print(f'BOX {box_n+1}:')
            for linha in boxes[box_n]:
                print(*linha)
            print()

# CONTABILIZANDO OS POKEMONS
qtd_pokemons=0
for n in range(len(boxes)):
    for i in range(5):
        for j in range(6):
            if boxes[n][i][j]==1:
                qtd_pokemons+=1

# IMPRIMINDO O RELATÓRIO FINAL
print('RELATÓRIO FINAL:')
print()
print(f'BOXES: {len(boxes)}')
print(f'POKEMONS: {qtd_pokemons}')
