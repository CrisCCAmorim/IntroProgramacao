construtor1=input()
posicao1=input()
salario1=int(input())
pontuacao1=0

construtor2=input()
posicao2=input()
salario2=int(input())
pontuacao2=0

if construtor1=='Red Bull':
    pontuacao1=+3
elif construtor1=='McLaren':
    pontuacao1=+2
    if posicao1=='1':
        pontuacao1=+3
        pontuacao1=pontuacao1 + (salario1//4)
    elif posicao1=='2':
        pontuacao1=+2
        pontuacao1=pontuacao1 + (salario1//4)
    else:
        pontuacao1=0
elif construtor1=='Mercedes': 
    pontuacao1=+1
    if posicao1=='1':
        pontuacao1=+3
        pontuacao1=pontuacao1 + (salario1//4)
    elif posicao1=='2':
        pontuacao1=+2
        pontuacao1=pontuacao1 + (salario1//4)
    else:
        pontuacao1=0
elif construtor1=='Aston Martin':
    pontuacao1=+1
    if posicao1=='1':
        pontuacao1=+3
        pontuacao1=pontuacao1 + (salario1//4)
    elif posicao1=='2':
        pontuacao1=+2
        pontuacao1=pontuacao1 + (salario1//4)
    else:
        pontuacao1=0
elif construtor1=='Ferrari':
    pontuacao1=0
else:
    if posicao1=='1':
        pontuacao1=+3
        pontuacao1=pontuacao1 + (salario1//4)
    elif posicao1=='2':
        pontuacao1=+2
        pontuacao1=pontuacao1 + (salario1//4)
    else:
        pontuacao1=0

if construtor2=='Red Bull':
    pontuacao2=+3
elif construtor2=='McLaren':
    pontuacao2=+2
    if posicao2=='1':
        pontuacao2=+3
        pontuacao2=pontuacao2 + (salario2//4)
    elif posicao2=='2':
        pontuacao2=+2
        pontuacao2=pontuacao2 + (salario2//4)
    else:
        pontuacao2=0
elif construtor2=='Mercedes': 
    pontuacao2=+1
    if posicao2=='1':
        pontuacao2=+3
        pontuacao2=pontuacao2 + (salario2//4)
    elif posicao2=='2':
        pontuacao2=+2
        pontuacao2=pontuacao2 + (salario2//4)
    else:
        pontuacao2=0
elif construtor2=='Aston Martin':
    pontuacao2=+1
    if posicao2=='1':
        pontuacao2=+3
        pontuacao2=pontuacao2 + (salario2//4)
    elif posicao2=='2':
        pontuacao2=+2
        pontuacao2=pontuacao2 + (salario2//4)
    else:
        pontuacao2=0
elif construtor2=='Ferrari':
    pontuacao1=0
else:
    if posicao2=='1':
        pontuacao2=+3
        pontuacao2=pontuacao2 + (salario2//4)
    elif posicao2=='2':
        pontuacao2=+2
        pontuacao2=pontuacao2 + (salario2//4)
    else:
        pontuacao2=0

if pontuacao1==0 and pontuacao2==0:
    print('Depois de tantas temporadas, o Sainz vai descançar em 2025.')
elif pontuacao1>pontuacao2:
    print(f'SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor1}, que pontuou {pontuacao1}.')
elif pontuacao2>pontuacao1:
    print(f'SMOOOOTH OPERATOOR! Sainz vai correr pela {construtor2}, que pontuou {pontuacao2}.')
else:
    print('As duas são ótimas opções! Vamos, Sainz!!')