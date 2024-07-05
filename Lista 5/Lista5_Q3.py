def busca_palavra(string, palavra):
    len_string = len(string)
    len_palavra = len(palavra)

    #se o comprimento da string for menor que o da palavra, a palavra não pode estar contida
    if len_string < len_palavra:
        return False

    # Verifica se a substring da string atual começa com a palavra
    if string[:len_palavra] == palavra:
        return True
    else:
        # Caso não seja igual, avança na string recursivamente
        return busca_palavra(string[1:], palavra)



linha_orc=input()
i=1
achou_senha=False
frase=''

while frase!='Decifra-me ou te devoro!' and achou_senha==False:
    frase=input()
    if frase!='Decifra-me ou te devoro!':
        palavras_frase=frase.split(' ')
        status_palavras=[]          #   lista que vai conter True ou False para cada palavra da frase, indicando se ela está ou não na linha orc
        
        for palavra in palavras_frase:      #   Armazenando o status de cada palavra
            status=busca_palavra(linha_orc,palavra)
            status_palavras.append(status)
        
        n_false=0
        for status in status_palavras:      # verificando se todas as palavras estão na linha orc
            if status==False:
                n_false+=1
        if n_false==0:
            achou_senha=True

        if achou_senha==False:
            i+=1
        else:
            print(f'Já sei, a senha é a frase número {i}')

if frase=='Decifra-me ou te devoro!' and achou_senha==False:        # Nenhuma frase serviu como senha
    print('Pensou que me enganaria? A magia da recursão me disse que a senha não pode ser nenhuma dessas')