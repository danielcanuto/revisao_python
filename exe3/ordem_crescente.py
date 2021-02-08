def crescente(vezes):
    lista = []
    temp = None
    cresc = True
    for n in range(vezes):
        num = int(input("Digite um Numero: \n>>"))
        if len(lista) == 0:
            lista.append(num)
            temp = num
        else:  
            if temp > num:
                lista.append(num)
                temp = num
                cresc = False
            else:
                lista.append(num)
                temp = num
    if cresc == True:
        return "crescente"
    else:
        return("Não está em ordem crescente")
            
def main(quantidade):
    print(crescente(quantidade))

main(3)