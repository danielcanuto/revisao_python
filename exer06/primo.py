def n_primo(n):
    for x in range(2, n):
        if n % x == 0:
            return("não primo")
    else:
        return('primo')


print(n_primo(int(input("Digite um numero: "))))
