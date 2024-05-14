n=int(input())
aprovacao=0
reprovacao=0
abstencao=0

for i in range(0,n,1):
    resp=input()
    if resp=='Adorei a troca de nome! Ficou mais legal e próximo dos fãs!!!':
        aprovacao+=1
    elif resp=='Não gostei. Muito sem graça, onde já se viu nome com duas letras?':
        reprovacao+=1
    else:
        abstencao+=1

if n!=0:
    print('A pesquisa terminou e os resultados foram os seguintes:')
    print(f'Para taxa de aprovação: {(aprovacao/n)*100 :.2f}')
    print(f'Taxa de rejeição: {(reprovacao/n)*100 :.2f}')
    print(f'Taxa de abstenção: {(abstencao/n)*100 :.2f}')
else:
    print('A pesquisa terminou e os resultados foram os seguintes:')
    print(f'Para taxa de aprovação: {(aprovacao)*100 :.2f}')
    print(f'Taxa de rejeição: {(reprovacao)*100 :.2f}')
    print(f'Taxa de abstenção: {(abstencao)*100 :.2f}')

if aprovacao>reprovacao:
    print('YES!!! Sabia que as pessoas gostariam!')
elif aprovacao<reprovacao:
    print('Ops... Por essa eu não esperava.')
else:
    print('Bom... Vou olhar para o copo meio cheio!')