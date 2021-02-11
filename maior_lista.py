def maior_elemento(lista):
    maior = lista[0]
    for x in lista:
        if x > maior:
            maior = x
            print(x)
    return maior

b = [ -15, -5, 0, -2]
x = [5, 9, 2, 8, 8, 15, 1, 5]
print(maior_elemento(x))
print(maior_elemento(b))
