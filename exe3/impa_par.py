def impar_par(numero):
    if numero == 0:
        return 'número neutro'
    else:
        if numero % 2 == 0:
            return 'par'
        else:
            return 'ímpar'


def main():
    n = int(input("Digite um Número: "))
    print(impar_par(n))


main()
