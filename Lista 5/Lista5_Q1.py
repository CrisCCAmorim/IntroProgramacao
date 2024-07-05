def login(n):
    if n==0:
        return n
    elif n%2==0:
        return n*2 + login(n-1)
    elif n%2==1:
        return n*3 + login(n-1)

def fatorial(n):
    if n==0:
        return 1
    else:
        return n*fatorial(n-1)


entrada=input().split(':')
log_in=''
senha=''

for num in entrada:
    l_n=str(login(int(num)))
    log_in=log_in+l_n

    s_n=str(fatorial(int(num)))
    senha=senha+s_n

print('As credenciais de acesso da área secreta da fortaleza foram decodificadas com sucesso!')
print(f'Login: {log_in}')
print(f'Senha: {senha}')