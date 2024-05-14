votos_beyonce=0
votos_taylor=0
qtd_alunos=int(input())

for i in range(0,qtd_alunos,1):
  voto=input()
  if voto=='beyonce':
    votos_beyonce+=1
    print(f'Aluno {i+1} votou na Beyoncé.')
  else:
    votos_taylor+=1
    print(f'Aluno {i+1} votou na Taylor Swift.')

print(f'Contagem de votos:\nTaylor Swift: {votos_taylor} votos\nBeyoncé: {votos_beyonce} votos')

if votos_beyonce==votos_taylor:
    print('Empate! Iniciando rodada de debate.\nAlunos, agora é a sua chance de convencer os outros a mudar de voto!')
    for i in range(0,qtd_alunos,1):
        mudanca=input()
        if mudanca=='sim':
            novo_voto=input()
            if novo_voto=='beyonce':
                print(f'Aluno {i+1} mudou seu voto para Beyoncé.')
                votos_beyonce+=1
            else:
                print(f'Aluno {i+1} mudou seu voto para Taylor Swift.')
                votos_taylor+=1
        else:
            print(f'Aluno {i+1} não mudou seu voto.')
    print(f'Nova contagem de votos após o debate:\nTaylor Swift: {votos_taylor} votos\nBeyoncé: {votos_beyonce} votos')

if votos_beyonce>votos_taylor:
    print(f'Beyoncé venceu com {votos_beyonce} votos! Será que Kanye West estava certo?')
elif votos_beyonce<votos_taylor:
    print(f'Taylor Swift venceu com {votos_taylor} votos! Kanye West tá irritado com isso.')
else:
    print('Aldo, como presidente do evento, tem o voto decisivo.')
    voto_aldo=input()
    if voto_aldo=='beyonce':
        print('Beyoncé é a vencedora com o voto decisivo de Aldo! Será que Kanye West estava certo?')
    else:
        print('Taylor Swift é a vencedora com o voto decisivo de Aldo! Kanye West tá irritado com isso.')
