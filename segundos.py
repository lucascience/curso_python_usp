segundos = input('Por favor, entre com o número de segundos que deseja converter: ')

dias = int(segundos) // 86400
segundos_rest = int(segundos) % 86400
horas = segundos_rest // 3600
segundos_rest = segundos_rest % 3600
minutos = segundos_rest // 60
segundos_rest = segundos_rest % 60

print(dias, 'dias,', horas, 'horas,', minutos, 'minutos e', segundos_rest, 'segundos.')
