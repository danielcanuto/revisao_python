def inverterdo(lista):
    n_lista = []
    x = len(lista)
    for i in range(len(lista)):
        if lista[x] >= 1:
            n_lista.append(lista[x])
        x -= 1
    return n_lista

a = [1, 5, 9, 3, 4]
print(inverterdo(a))