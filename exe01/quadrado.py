
def area(lado):
    return lado ** 2
    

def perimetro(lado):
    return lado * 4

def calcula_perimento_area_quadrado(lado):
    return f'perímetro: {perimetro(lado)} - área: {area(lado)}'

lado_tamanho = int(input("Digite o valor correspondente ao lado de um quadrado: "))
print(calcula_perimento_area_quadrado(lado_tamanho))
