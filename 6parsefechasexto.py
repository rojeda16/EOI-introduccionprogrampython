from datetime import datetime
fecha = "10-11-2022"
fecha1 = datetime.strptime(fecha, '%M-%d-%Y').date()

print (f"fecha1:, {fecha}")
print(f"fecha1 {fecha1.day}/{fecha1.month}/{fecha1.year}")
