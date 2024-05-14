nome=input()
qtd_music=int(input())
mais_ouvida=''
maior_num=0
menos_ouvida=''
menor_num=0

if qtd_music==0:
    print(f'{nome} é team Taylor e não ouviu Kanye West')
elif qtd_music==1:
    musica=input()
    num_streams=input()
    print(f'A única música que {nome} ouviu foi {musica} com {num_streams} streams')
else:
    for i in range(0,qtd_music,1):
        musica=input()
        num_streams=int(input())
        
        if maior_num==0 and menor_num==0:
            maior_num=num_streams
            mais_ouvida=musica
            menor_num=num_streams
            menos_ouvida=musica
        elif num_streams>maior_num:
            maior_num=num_streams
            mais_ouvida=musica
        elif num_streams<menor_num:
            menor_num=num_streams
            menos_ouvida=musica
    if maior_num==menor_num:
        print(f'A música que {nome} mais ouviu foi {mais_ouvida} com {maior_num} streams')
    else:
        print(f'A música que {nome} mais ouviu foi {mais_ouvida} com {maior_num} streams')
        print(f'A música que {nome} menos ouviu foi {menos_ouvida} com {menor_num} streams')

