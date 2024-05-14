n=int(input())
pontos=0

for i in range(0,n,1):
    pratica=input()

    #boas práticas
    if pratica=='Programar utilizando uma boa IDE':
        pontos+=3
    elif pratica=='Códigos limpos e organizados':
        pontos+=10
    elif pratica=='Nomenclatura objetiva e de fácil identificação de variáveis':
        pontos+=7
    elif pratica=='Assistir às aulas do REDU':
        pontos+=10
    elif pratica=='Comentários significativos':
        pontos+=5
    elif pratica=='Evitar repetições desnecessárias de códigos':
        pontos+=5
    elif pratica=='Tirar dúvidas com os monitores e professores':
        pontos+=10
    #más práticas
    elif pratica=='Programar sem utilizar IDE':
        pontos-=5
    elif pratica=='Código bagunçado e mal estruturado':
        pontos-=6
    elif pratica=='Nomenclatura confusa e difícil de identificar variáveis':
        pontos-=5
    elif pratica=='Não tirar dúvidas com professores e monitores':
        pontos-=10

if n!=0:
    media=pontos/n
    if media<0:
        media=0
    elif media>10:
        media=10
else:
    media=0

if media<3:
    print('É melhor voltar a cantar mesmo!')
elif media>=3 and media<7:
    print('Vai precisar se esforçar um pouco mais, meu cantor!')
elif media==7:
    print('Na conta certa!')
elif media>7 and media<9:
    print('Nasceu para programar!')
else:
    print('Já pode ser chamado de Kanye, the dev, West!')
