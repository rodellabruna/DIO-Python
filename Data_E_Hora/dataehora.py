from datetime import date, datetime, time

#datetime.date()

data = date(2023, 7, 10)
print(data)

dia = date.today()
print(dia)
print(date.today())

print(datetime.today())

preciso_Data_e_Hora = datetime(2022, 2, 1, 10, 5, 3)
print(preciso_Data_e_Hora)


preciso_Data_e_Hora = datetime(2022, 2, 1)
print(preciso_Data_e_Hora)

hora = time(10, 20, 0)
print(hora)