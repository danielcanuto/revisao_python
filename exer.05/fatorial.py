def fatorial(n):
    if n ==0:
        return 1
    
    else:    
        fat= n2 = n
        
        i = 1
        while i < n2 - 1:
            n -= 1
            fat = fat * n 
            i += 1
        return fat

def teste_fat():
    if fatorial(1) == 1:
        print('Funciona para 1')
    else:
        print(' Nao funciona para 1')

    if fatorial(2) == 2:
        print('Funciona para 2')
    else:
        print(' Nao funciona para 3')
    
    if fatorial(0) == 1:
        print('Funciona para 0')
    else:
        print(' Nao funciona para 0')

n = int(input("Digite um número: "))

print(fatorial(n))