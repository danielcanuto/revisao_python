def estrategia(n, m):
    if (n - m) % (m + 1) == 0:
        return m
    else:
        if n > m + 1:
            return m - 1


def computador_escolhe_jogada(n, m):
    print()
    if n == 1:
        print("O computador tirou uma peça.")
        print("Fim do jogo! O computador ganhou!")
        return n
    else:
        if m >= n:
            print(f"O computador tirou {n} peças.")
            print("Fim do jogo! O computador ganhou!")
            return n
# aqui aplicar a regra
        else:
            qnt = estrategia(n, m)
            print(f"O computador tirou {qnt} peças.")
            print(f"Agora restam {n - qnt} peças no tabuleiro.")
            return qnt


def usuario_escolhe_jogada(n, m):
    qnt = int(input("Quantas peças você vai tirar? "))
    while 0 >= qnt or qnt > m:
        print(f"Você precisa escolher um valor entre 1 e {m}!!")
        print("TENTE NOVAMENTE.")
        qnt = int(input("Quantas peças você vai tirar? "))

    print(f'Voce tirou {qnt} peças.')
    n -= qnt

    if n == 1:
        print("Agora resta apenas uma peça no tabuleiro.")
    else:
        print(f"Agora restam {n} peças no tabuleiro.")
    return qnt


def campeonato():
    cont = 1
    vc = 0
    cpu = 0

    while cont < 4:
        print("Voce escolheu um campeonato!")
        print(f"**** Rodada {cont} ** **")
        partida()
        cont += 1
        cpu += 1
        # resta pontua
    print("**** Final do campeonato! ****")
    print(f"Placar: Você {vc} X {cpu} Computador")


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    comeca = quem_comeca(n, m)

    if comeca == "vc":
        while n > 0:
            n -= usuario_escolhe_jogada(n, m)
            if n > 0:
                n -= computador_escolhe_jogada(n, m)

    elif comeca is None:
        pass

    elif comeca == "pc":
        while n > 0:
            n -= computador_escolhe_jogada(n, m)
            if n > 0:
                n -= usuario_escolhe_jogada(n, m)


"""
    As funções completas estão abaixo!!!
"""


def abertura():
    print("1 - para jogar uma partida isolada\
        \n2 - para jogar um campeonato")
    tipo_jogo = input(".>> ")
    return tipo_jogo


def quem_comeca(n, m):
    if n % (m + 1) == 0:
        print("Você começa!")
        return "vc"

    else:
        print("Computador começa!")
        return "pc"


def partida_isolada():
    print("Partida treino")
    partida()


def main():
    print("Bem-vindo ao jogo do NIM! Escolha: ")
    tipo_jogo = abertura()

    if tipo_jogo == "1":
        partida_isolada()

    elif tipo_jogo == "2":
        campeonato()
    else:
        print("Comando inválido\nTente novamente")
        main()


main()
