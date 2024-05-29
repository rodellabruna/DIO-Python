from datetime import timedelta, datetime, date, time

tipo_carro = 'M' # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
# data_atual = datetime.today() 
data_atual = datetime.now() #ja vem com timezone

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou em: {data_atual} \nFicará pronto em: {data_estimada}")

elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou em: {data_atual} \nFicará pronto em: {data_estimada}")

else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou em: {data_atual} \nFicará pronto em: {data_estimada}")
    
    
#timesdelta da para passar dias, semanas, horas

print(date.today() - timedelta(days=1))

resultado = datetime(2024, 5, 28, 23, 19, 20) - timedelta(hours=1)
print(resultado.time())


print(datetime.now())
print(datetime.now().date())
    