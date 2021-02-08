def soma_digitos(numero_str):
    soma = 0
    
    for i in numero_str:
        soma += int(i)
    return soma

def soma_digitos2(numero_str):
    if int(numero_str) == 0:
        return 0
    else:
        soma = 0 
        cont = 0
        while cont < len(numero_str):
            soma += int(numero_str[cont])
            
            cont += 1
        return soma

print(soma_digitos2(input("digite um numero: "))) 
# soma_digitos('1111111111')