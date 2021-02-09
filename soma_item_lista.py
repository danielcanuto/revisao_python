def soma_elementos(lista):
    total = 0
    for x in lista:
        total += x
    return total


a = [15, 25, 9, 4, -13, 1, 1, 2, 2, 3, 3]

print(soma_elementos(a))
