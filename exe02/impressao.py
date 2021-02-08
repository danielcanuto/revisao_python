def cad_fatura():
    cliente = input("Digite o nome do cliente: ")
    dia_venc = input("Digite o dia de vencimento: ")
    mes_venc = input("Digite o mês de vencimento: ")
    
    valor =  input("Digite o valor da fatura: ")
    return f'Olá, {cliente}\nA sua fatura com vencimento em {dia_venc} de {mes_venc} no valor de R$ {valor} está fechada.'

print(cad_fatura())