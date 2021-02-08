def divisivel_3(numero):
    # if numero == 0:
    #     return 'número neutro'
    # else:
    if numero % 3 == 0:
        return 'Fizz'
    else:
        return str(numero)


def main():
    n = int(input("Digite um Número: "))
    print(divisivel_3(n))


main()
