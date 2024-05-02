vel_max=float(input())
tempo=input()

if tempo!='neblina':
    if vel_max>=250 and vel_max<=260:
        print('Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!')
    elif vel_max>=261 and vel_max<=285:
        print('Senna corria em Ímola, onde infelizmente fez sua última corrida.')
    elif vel_max>=286 and vel_max<=310:
        print('Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!')
else:
    if vel_max<250:
        print('Nesse dia, Senna corria em Mônaco, onde esteve no pódio 8 vezes!')
    elif vel_max>=250 and vel_max<=260:
        print('Senna corria em Ímola, onde infelizmente fez sua última corrida.')
    elif vel_max>=261 and vel_max<=285:
        print('Claramente Spa-Francorchamps, circuito no qual Senna venceu histórico duelo com Prost depois de três largadas!')
