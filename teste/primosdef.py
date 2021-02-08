def primo(n):
    for x in range(2, n):
        if (n % x) == 0:
            return False
    else:
        return True


def maior_primo(n):
    while n >= 2:
        if primo(n):
            return n
        else:
            n -= 1
