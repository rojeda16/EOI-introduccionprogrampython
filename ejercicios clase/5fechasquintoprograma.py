from datetime import datetime
datenow1 = datetime.now().date()
print("fecha1:", datenow1)
print("año fecha1:",datenow1.year)
print("mes fecha1:",datenow1.month)
print("dia fecha1:",datenow1.day)

datenow2= datetime.now()
print ("fecha:",datenow2)
print("Año:", datenow2.year)
print("Mes:", datenow2.month)
print("Dia:", datenow2.day)
print(f"Hora: {datenow2.hour}:{datenow2.minute}")
print("microsegundos fecha2",datenow2.minute)

datenow3= datetime.now()
print ("fecha:",datenow3)
print("Año:", datenow3.year)
print("Mes:", datenow3.month)
print("Dia:", datenow3.day)
print(f"Hora: {datenow2.hour}:{datenow3.minute}")
print("microsegundos fecha3",datenow3.minute)



