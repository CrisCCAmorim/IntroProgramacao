def mdc(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    else:
        if a == b:
            return a
        elif a > b:
            return mdc(a - b, b)
        else:
            return mdc(a, b - a)

qtd=int(input())
senha=0

for q in range(qtd):
    numeros=input().split(' ')
    result_mdc=mdc(int(numeros[0]),int(numeros[1]))
    print(f'O MDC entre {numeros[0]} e {numeros[1]} é {result_mdc}')
    senha+=result_mdc

print()
print(f'A senha final foi {senha}')