def devolve_dezena(numero):
    if len(numero) < 2:
        return "0"
    else:
        return numero[-2]
    
def main():
    numero = input("Digite um número inteiro: ")
    return f'O dígito das dezenas é {devolve_dezena(numero)}'

print(main())