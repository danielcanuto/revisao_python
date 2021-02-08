import math


def delta(a, b, c):
    return b ** 2 - 4 * a * c


def main():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    d = delta(a, b, c)

    if d < 0:
        return "esta equação não possui raízes reais"
    else:
        raiz1 = (- b + math.sqrt(d)) / (2 * a)
        if d == 0:
            return raiz1
        else:
            raiz2 = (- b - math.sqrt(d)) / (2 * a)
            if raiz1 < raiz2:
                return (raiz1, raiz2)
            else:
                return (raiz2, raiz1)


print(main())
