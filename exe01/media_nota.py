


def media(lista_notas):
    soma = 0
    for nota in lista_notas:
        soma += nota
    return soma / len(lista_notas)


# ordem = ['primeira', 'segunda', 'terceira', 'quarta']

def cadastro_nota():
    ordem_notas = {'primeira': 0, 'segunda': 0, 'terceira': 0, 'quarta': 0}
    notas = []
    for nota in ordem_notas:
        ordem_notas[nota] = float(input(f"Digite a {nota} nota:"))
        notas.append(ordem_notas[nota])

    return f'A média aritmética é { media(notas)}'

print(cadastro_nota())
