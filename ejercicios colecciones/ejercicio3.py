#Hacer un programa que procese un total de 100 personas y establecer cuantas son mujeres mayores de edad y cuantos hombres menores de edad. 
# Deberá sacar el hombre y la mujer con menor edad, el hombre y la mujer con mayor edad, 
# promedio de edades de las mujeres y promedio de edades de los hombres.

from random import randint


mujeresmayores = []
hombresmenores = []

for personas in range(1,101):
    edad=randint(1,100)
    if (edad >= 18):
        mujeresmayores.append(edad)
    elif(edad<18):
        hombresmenores.append(edad)

promediomujeres=sum(mujeresmayores)/len(mujeresmayores)
promediohombres=sum(hombresmenores)/len(hombresmenores)

print(mujeresmayores)
print(hombresmenores)

print(f"{len(mujeresmayores)} mujeres tienen 18 años o son mayores de 18 años")

print(f"{len(hombresmenores)} hombres son menores de 18 años")

print(f"La Mujer de mayor edad tiene {max(mujeresmayores)}")

print(f"La Mujer de menor edad tiene {min(mujeresmayores)}")

print(f"El hombre de menor edad tiene {min(hombresmenores)}")

print(f"El hombre de mayor edad tiene {max(hombresmenores)}")

print(promediomujeres)
print(promediohombres)