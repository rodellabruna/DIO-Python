from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2024-05-28 22:49"
mascara_ptbr = '%d/%m/%Y %a'
print(data_hora_atual)
print(data_hora_atual.strftime(mascara_ptbr))

print(type(data_hora_str))

mascara_en='%Y-%m-%d %H:%M'

print(type(datetime.strptime(data_hora_str, mascara_en)))
print(datetime.strptime(data_hora_str, mascara_en))
print(type(data_hora_str))


dataconvertida = datetime.strptime(data_hora_str, mascara_en)
print(dataconvertida)
print(type(dataconvertida))
print(dataconvertida.time())
print(dataconvertida.date())