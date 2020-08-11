from datetime import datetime,  date, timedelta, time

ahora = datetime.now()
#print(type(ahora))
#print(ahora.utcnow())
#2020-08-10 23:12:00"
#print(f'{ahora.year}-{ahora.month}-{ahora.day} {ahora.hour}:{ahora.minute}:{ahora.second}')

#creamos fecha con parametros

hoy = datetime.today()
print(hoy)
formato_date = "%Y-%m-%d"
formato_datetime = "%Y-%m-%d %H:%M:%S"
#print(f'fecha formato date: {hoy.strftime(formato_date)}')
#print(f'fecha formato datetime: {hoy.strftime(formato_datetime)}')

#convertir una cadena a un objeto datatime
objeto_datetime = datetime.strptime('2020-08-04', formato_date)
#print(type(objeto_datetime))

#operacion por fechas
fecha = date.today()
print(f'fecha menos 1 dia  {fecha - timedelta(weeks=8)} ')

fecha1 = datetime.now()
fecha2 = datetime(2019,11,5,0,0,0)

diferencia = fecha1-fecha2
print (f'{diferencia.days}')

print(f"dia de la semana {datetime.weekday(fecha1)}")

#convertir a timestamp

print(f"fecha= {fecha1} | {datetime.timestamp(fecha1)}")

#convertir de timestamp
print(f"datetime")