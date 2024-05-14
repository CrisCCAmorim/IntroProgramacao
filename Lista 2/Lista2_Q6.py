from decimal import Decimal, getcontext
getcontext().prec = 15

qtd_veiculos=int(input())
acidente=input()
distancia_total=float(input())
codigo_serializacao=input()

#Calculando opcao A

dist_jato=Decimal(0.8*distancia_total)
tempo_jato=Decimal(dist_jato/1089)

dist_blindado=Decimal(0.2*distancia_total)
tempo_blindado=Decimal(dist_blindado/60)

if acidente=='nao':
    tempo_transito = Decimal(0.01*qtd_veiculos)
else:
    tempo_transito = Decimal(0.01*qtd_veiculos) + Decimal(1/3)

tempo_a = tempo_jato + tempo_blindado + tempo_transito
tempo_a=Decimal(tempo_a*60)

#Calculando opcao B

tempo_onibus=Decimal(distancia_total/40)

tempo_b = tempo_onibus + tempo_transito
tempo_b=Decimal(tempo_b*60)

#Calculando opcao C

tempo_c = Decimal(5*(distancia_total/360))
tempo_c=Decimal(tempo_c*60)

#Desserializando o codigo

codigo_desserializado=''
for i in codigo_serializacao:
    codigo_desserializado=codigo_desserializado+i
    if int(i)%2==0:
        codigo_desserializado=codigo_desserializado+'23'
    else:
        codigo_desserializado=codigo_desserializado+'78'

#Outputs
print('Análise das opções de transporte até o show!')
print(f'Opção A - Você chegará ao show em {tempo_a:.1f} minutos')
print(f'Opção B - Você chegará ao show em {tempo_b:.1f} minutos')
print(f'Opção C - Você chegará ao show em {tempo_c:.1f} minutos')
print(f'---\nSenha de serialização transformada: {codigo_desserializado}, guarde com segurança!')