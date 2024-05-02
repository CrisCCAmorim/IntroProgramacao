piloto=input()
distancia=float(input())
tempo=float(input())

velocidade=distancia/tempo

if velocidade>227:
    print(piloto,'se deu muito bem na prova de hoje!!')
elif velocidade==227:
    print(piloto,'teve um ótimo resultado. Mas, acredito que temos potencial para melhorar um pouco mais!')
else:
    print(piloto,'não se deu tão bem. É preciso melhorar isso!')