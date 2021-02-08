def divisivel_5(numero):

    if numero % 5 == 0:
        return True
    else:
        return False


def divisivel_3(numero):
    if numero % 3 == 0:
        return True
    else:
        return False


def fizzbuzz(n):
    # n = int(input("Digite um Número: "))
    if divisivel_5(n) == True:
        if divisivel_3(n) == True:
            return 'FizzBuzz'
        else:
            return 'Buzz'

    if divisivel_3(n) == True:
        return 'Fizz'
    else:
        return n


# print(fizzbuzz(89))
