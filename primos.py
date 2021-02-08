def primo(n):
    for x in range(2, n):
        if (n % x) == 0:
            return False
    else:
        return True

def n_primos(n):
    if n < 2:
        print("tente novamente com um numero maior que 1")
        n_primo(n)
    else:
        cont = 0
        for x in range(n):
            primo(x)
            cont += 1
    return cont