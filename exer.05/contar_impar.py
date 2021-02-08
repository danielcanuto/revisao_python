
def cont_impar(quant):
    n = 1
    while quant > 0:    
        if n % 2 != 0:
            print(n)
            quant -= 1 
        n += 1
        
            

n = int(input("Digite um numero: "))
cont_impar(n)