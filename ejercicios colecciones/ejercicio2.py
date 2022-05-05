#Hacer un programa que procese las edades de 100 personas. 
# Deberá decir cuantas tienen más de (≥18) y cuál es la persona con menor edad y cuál es la persona con mayor edad. 
# También deberá mostrar el porcentaje de edades de las 100 personas.
from random import randint

personasmayores = []
personasmenores = []

for personas in range(1,101):
    edad=randint(1,100)
    if (edad >= 18):
        personasmayores.append(edad)
    elif(edad<18):
        personasmenores.append(edad)

print(personasmayores)
print(personasmenores)

print(f"{len(personasmayores)} personas tienen 18 años o son mayores de 18 años")
print(f"El {len(personasmayores)} % son Mayores")
print(f"{len(personasmenores)} personas son menores de 18 años")
print(f"El {len(personasmenores)} % son Menores")
print(f"La persona de mayor edad tiene {max(personasmayores)}")
print(f"La persona de menor edad tiene {min(personasmenores)}")