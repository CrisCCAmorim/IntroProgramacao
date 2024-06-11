num_animais=int(input())
catalogo_animais=[]

while len(catalogo_animais)<num_animais:
    comando=input()

    if comando=='REGISTRA':
        registro = input()

        #checando se o animal está presente na lista
        presente = False
        for animal in catalogo_animais:
            if animal==registro:
                presente=True

        #registrando e informando
        if presente==True:
            print(f'{registro} já foi registrado antes!')
        else:
            catalogo_animais.append(registro)
            print(f'{registro} registrado com sucesso.')

    elif comando=='CORRIGE':
        if len(catalogo_animais)==0:
            print('O catálogo ainda está vazio.')
        else:
            catalogo_animais.pop()
            print('Último registro apagado com sucesso.')

    elif comando=='REINICIA':
        catalogo_animais=[]
        print('Catálogo redefinido com sucesso.')

else:
    print('Todos os animais foram registrados!')

#imprimindo o catálogo de animais

print('\nCatálogo de animais:')
for i in range(0,num_animais,1):
    print(f'{i+1}º: {catalogo_animais[i]}')