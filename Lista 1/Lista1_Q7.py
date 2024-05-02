piloto_a=input()
tempo_a=float(input())

piloto_b=input()
tempo_b=float(input())

piloto_c=input()
tempo_c=float(input())

if tempo_a<tempo_b and tempo_a<tempo_c:
    primeiro_lugar=piloto_a
    primeiro_tempo=tempo_a
    if tempo_b<tempo_c:
        segundo_lugar=piloto_b
        segundo_tempo=tempo_b
        terceiro_lugar=piloto_c
        terceiro_tempo=tempo_c
    else:
        segundo_lugar=piloto_c
        segundo_tempo=tempo_c
        terceiro_lugar=piloto_b
        terceiro_tempo=tempo_b
elif tempo_b<tempo_a and tempo_b<tempo_c:
    primeiro_lugar=piloto_b
    primeiro_tempo=tempo_b
    if tempo_a<tempo_c:
        segundo_lugar=piloto_a
        segundo_tempo=tempo_a
        terceiro_lugar=piloto_c
        terceiro_tempo=tempo_c
    else:
        segundo_lugar=piloto_c
        segundo_tempo=tempo_c
        terceiro_lugar=piloto_a
        terceiro_tempo=tempo_a
else:
    primeiro_lugar=piloto_c
    primeiro_tempo=tempo_c
    if tempo_a<tempo_b:
        segundo_lugar=piloto_a
        segundo_tempo=tempo_a
        terceiro_lugar=piloto_b
        terceiro_tempo=tempo_b
    else:
        segundo_lugar=piloto_b
        segundo_tempo=tempo_b
        terceiro_lugar=piloto_a
        terceiro_tempo=tempo_a

print('E o Pódio do GP de Mônaco é:')
print(primeiro_lugar,'está no lugar mais alto do pódio com tempo de',primeiro_tempo,'horas de corrida.')
print(segundo_lugar,'está no segundo lugar do pódio com tempo de',segundo_tempo,'horas de corrida.')
print(terceiro_lugar,'está no terceiro lugar do pódio com tempo de',terceiro_tempo,'horas de corrida.')
print('Galvão, temos um momento histórico da Fórmula 1,',primeiro_lugar,'acaba de fazer história no GP de Mônaco ao terminar a corrida com',primeiro_tempo,'horas de prova.')