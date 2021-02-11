def recebe_numero():
    num = int(input("Digite um número: "))
    return num

def imprime_list_passo(lista):
    for n in lista:
        print(n)

def inverterdo():
    lista = []
    n_lista = []
    num = 1
    while num != 0:
        num = recebe_numero()
        if num != 0:
            lista.append(num)
    n = len(lista)
    for i in range(len(lista)):
        n -= 1
        n_lista.append(lista[n])

    return imprime_list_passo(n_lista)


inverterdo()
