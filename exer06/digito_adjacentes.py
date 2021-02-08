

def adjacentes(num_str):
    temp = 'z'
    adj = False
    for x in num_str:
        if x == temp:
            adj = True
        temp = x
    if adj == True:
        return "sim"
    else:
        return "não"

print(adjacentes(input("Digite um numero: ")))