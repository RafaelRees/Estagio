# Definição de Horário AM/PM
#   AM = 00:00:00AM até 11:59:59AM 
#   PM = 00:00:00PM até 11:59:59PM
# Portanto horas não podem ultrapassar de 11 e minutos/segundos de 59
# Horas só positivas pois não existe negativa

Tempo = str(input('Digite as horas no formato hh:mm:ssAM/PM: '))

Hora = int(Tempo[0:2])
Min = int(Tempo[3:5])
Seg = int(Tempo[6:8])
AMPM = str(Tempo[8:10])

while Hora < 0 or Hora > 11:
    Hora = int(input('insira valores validos de horas 0 a 11:'))
while Min < 0 or Min > 59:   
    Min = int(input('insira os minutos de 0 a 59: '))
while Seg < 0 or Seg > 59: 
    Seg = int(input('insira os segundos de 0 a 59: '))
if AMPM == "AM": 
    print('{}:{}:{}'.format(Hora, Min, Seg))
else: 
    print('Horas: {}:{}:{}'.format(Hora+12, Min, Seg))