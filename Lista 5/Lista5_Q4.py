def soma_itens(lista):
    total = 0
    for elemento in lista:
        if isinstance(elemento, list):
            total += soma_itens(elemento)
        else:
            total += elemento
    return total

def print_lista(lista):
    for item in lista:
        if isinstance(item, list):
            print_lista(item)
    
    soma = soma_itens(lista)
    print(soma, end=' -> ')
    print(lista)
 
lista=eval(input())
print_lista(lista)