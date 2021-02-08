def divisivel_5(numero):

    if numero % 5 == 0:
        return True
    else:
        return str(numero)

def divisivel_3(numero):
    if numero % 3 == 0:
        return True
    else:
        return str(numero)

def main():
    n = int(input("Digite um Número: "))
    if divisivel_5(n) == True and divisivel_3(n) == True:
        print("FizzBuzz")
    else:
        print(f'{n}')
main()