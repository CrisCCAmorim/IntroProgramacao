acumulada_hamilton=int(input())
ultima_hamilton=int(input())

acumulada_verstappen=int(input())
ultima_verstappen=int(input())

acumulada_bottas=int(input())
ultima_bottas=int(input())

if ultima_hamilton<=10:
    total_hamilton = acumulada_hamilton + 5
else:
    total_hamilton = acumulada_hamilton

if ultima_verstappen<= 10:
    total_verstappen = acumulada_verstappen + 5
else:
    total_verstappen = acumulada_verstappen

if ultima_bottas<= 10:
    total_bottas = acumulada_bottas + 5
else:
    total_bottas = acumulada_bottas

#condicoes de vitoria de Hamilton
if total_hamilton>total_bottas and total_hamilton>total_verstappen:
    print('Lewis Hamilton ganhou a competição com',total_hamilton,'pontos!')
elif total_hamilton==total_verstappen and total_hamilton>=total_bottas:
    print('Lewis Hamilton ganhou a competição com',total_hamilton,'pontos!')
elif total_hamilton==total_bottas and total_hamilton>=total_verstappen:
    print('Lewis Hamilton ganhou a competição com',total_hamilton,'pontos!')

#condicoes de vitoria de Verstappen
elif total_verstappen>total_hamilton and total_verstappen>total_bottas:
    print('Max Verstappen ganhou a competição com',total_verstappen,'pontos!')
elif total_verstappen==total_bottas and total_verstappen>=total_hamilton:
    print('Max Verstappen ganhou a competição com',total_verstappen,'pontos!')

#condicao para vitoria de bottas
elif total_bottas>total_hamilton and total_bottas>total_verstappen:
    print('Valtteri Bottas ganhou a competição com',total_bottas,'pontos!')