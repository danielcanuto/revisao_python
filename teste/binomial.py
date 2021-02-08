from exe3.impa_par import main


def fatorial(n):
    if n == 0:
        return 1

    else:

        fat = n2 = n
        i = 1
        while i < n2 - 1:
            n -= 1
            fat = fat * n
            i += 1
        return fat


def fatorial1(n):
    if n < 0:
        return 0

    fat = 1
    while (n > 1):
        fat = fat * n
        n -= 1
    return fat


def binomial(n, k):
    if k <= n:
        return fatorial1(n) / fatorial1(k) * fatorial1(n-k)


if __name__ == "__main__":
    print(fatorial1(0))
