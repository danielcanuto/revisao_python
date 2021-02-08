import math


def pontos(x, y):
    return(x, y)


def distancia(ponto1, ponto2):
    return math.sqrt(
        ((ponto1[0] - ponto1[1]) ** 2) + ((ponto2[0] - ponto2[1]) ** 2)
    )


def recebe():
    n1 = int(input("digite a cordenada x: "))
    n2 = int(input("digite a cordenada y: "))
    return pontos(n1, n2)


def main():
    ponto1 = recebe()
    ponto2 = recebe()
    dist = distancia(ponto1, ponto2)
    if dist >= 10:
        print("longe")
    else:
        print("perto")


main()
