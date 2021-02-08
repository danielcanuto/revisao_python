def rec_second_retrum_hoars(segundos):
    dias = segundos // 86400
    segundos_rest = segundos % 86400
    horas = segundos_rest // 3600
    segundos_rest = segundos_rest % 3600
    minutos = segundos_rest // 60
    rsegundos = segundos_rest % 60
    return f'{dias} dias, {horas} horas, {minutos} minutos e {rsegundos} segundos.'

def recebe_dado_seg():
    segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
    return segundos
print(rec_second_retrum_hoars(recebe_dado_seg()))