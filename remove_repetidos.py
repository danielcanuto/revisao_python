def remove_repetidos(lista):
    nova_lista = []
    for x in lista:
        if x not in nova_lista:
            nova_lista.append(x)

    return sorted(nova_lista)

# def ordenar

d = [15, 25, 9, 4, -13, 1, 1, 2, 2, 3, 3]
print(remove_repetidos(d))
