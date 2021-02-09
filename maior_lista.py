def maior_elemento(lista):
    maior = 0
    for x in lista:
        if x > maior:
            maior = x
    return maior
