pontos_charles=int(input())
pontos_max=int(input())

dif_pontos= pontos_charles-pontos_max

if pontos_charles<1:
    print('Oxe! E vai morrer por causa de 25 pontos?')
else:
  if pontos_charles==25:
      print('O meu favorito venceu! Pode torar o aco Verstappen')
  elif pontos_charles<25 and pontos_charles>12:
      print('Esse Charles eh arretado mesmo')
  elif pontos_charles<15 and pontos_charles>8:
      print('Ele eh desenrolado demais')
      
  if dif_pontos<=4 and dif_pontos>=-4:
    print('Ta com a molestia, vai perder para Max Verstappen eh')
  elif dif_pontos>4:
    print('Deu o sangue')
    




