def maior(x, y):
    if x > y:
        return x
    else:
        return y


def maximo(x, y, z):
    a = maior(x, y)
    return maior(a, z)
