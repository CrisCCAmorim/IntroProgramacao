especies=["Anchova", "Atum", "Bagre", "Baiacu", "Cioba", "Enguia", "Esturjão", "Linguado", "Pepino-do-mar", "Polvo", "Salmão", "Sardinha", "Tilápia", "Truta", "Robalo"]

# PESCADOR 1 

#coletando nome e conquistas do pescador 1
pescador_conquistas=input().split(': ')
pescador1=pescador_conquistas[0]
conquistas1=pescador_conquistas[1].split(', ')
peixes1=[]

#coletando quais os peixes o pescador 1 pegou
peixe=''
while peixe!='FIM':
    peixe=input()
    if peixe!='FIM':
        peixes1.append(peixe)

#checando quantas espécies o pescador 1 pegou
qtd_especies=0
for especie in especies:
    if especie in peixes1:
        qtd_especies+=1

#checando as conquistas do pescador 1
pescador1_mentiu=False
if 'Pescador' in conquistas1:
    if qtd_especies<5:
        pescador1_mentiu=True
if 'Velho Marinheiro' in conquistas1:
    if qtd_especies<10:
        pescador1_mentiu=True
if 'Velho Pescador' in conquistas1:
    if qtd_especies<len(especies):
        pescador1_mentiu=True
if 'Deus Pescador' in conquistas1:
    if len(peixes1)<25:
        pescador1_mentiu=True
if pescador1_mentiu==True:
    print(f'{pescador1} é um mentiroso, ele não tem todas essas conquistas!')
else:
    print(f'{pescador1} realmente estava falando a verdade!!!')


# PESCADOR 2 

#coletando nome e conquistas do pescador 2
pescador_conquistas=input().split(': ')
pescador2=pescador_conquistas[0]
conquistas2=pescador_conquistas[1].split(', ')
peixes2=[]

#coletando quais os peixes o pescador 2 pegou
peixe=''
while peixe!='FIM':
    peixe=input()
    if peixe!='FIM':
        peixes2.append(peixe)

#checando quantas espécies o pescador 2 pegou
qtd_especies=0
for especie in especies:
    if especie in peixes2:
        qtd_especies+=1

#checando as conquistas do pescador 2
pescador2_mentiu=False
if 'Pescador' in conquistas2:
    if qtd_especies<5:
        pescador2_mentiu=True
if 'Velho Marinheiro' in conquistas2:
    if qtd_especies<10:
        pescador2_mentiu=True
if 'Velho Pescador' in conquistas2:
    if qtd_especies<len(especies):
        pescador2_mentiu=True
if 'Deus Pescador' in conquistas2:
    if len(peixes2)<25:
        pescador2_mentiu=True
if pescador2_mentiu==True:
    print(f'{pescador2} é um mentiroso, ele não tem todas essas conquistas!')
else:
    print(f'{pescador2} realmente estava falando a verdade!!!')


# PESCADOR 3

#coletando nome e conquistas do pescador 3
pescador_conquistas=input().split(': ')
pescador3=pescador_conquistas[0]
conquistas3=pescador_conquistas[1].split(', ')
peixes3=[]

#coletando quais os peixes o pescador 1 pegou
peixe=''
while peixe!='FIM':
    peixe=input()
    if peixe!='FIM':
        peixes3.append(peixe)

#checando quantas espécies o pescador 1 pegou
qtd_especies=0
for especie in especies:
    if especie in peixes3:
        qtd_especies+=1

#checando as conquistas do pescador 1
pescador3_mentiu=False
if 'Pescador' in conquistas3:
    if qtd_especies<5:
        pescador3_mentiu=True
if 'Velho Marinheiro' in conquistas3:
    if qtd_especies<10:
        pescador3_mentiu=True
if 'Velho Pescador' in conquistas3:
    if qtd_especies<len(especies):
        pescador3_mentiu=True
if 'Deus Pescador' in conquistas3:
    if len(peixes3)<25:
        pescador3_mentiu=True
if pescador3_mentiu==True:
    print(f'{pescador3} é um mentiroso, ele não tem todas essas conquistas!')
else:
    print(f'{pescador3} realmente estava falando a verdade!!!')