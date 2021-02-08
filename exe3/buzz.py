def divisivel_5(numero):
    # if numero == 0:
    #     return 'número neutro'
    # else:
    if numero % 5 == 0:
        return 'Buzz'
    else:
        return str(numero)

def main():
    n = int(input("Digite um Número: "))
    print(divisivel_5(n))
main()