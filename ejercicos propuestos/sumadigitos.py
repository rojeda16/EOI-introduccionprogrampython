#Algoritmo SumaDigitos
numero = int (input("ingresa numero"))
resul= 0

while  (numero != 0):
    resul +=(numero % 10)
    numero = numero//10
	
print("El resultado es: ", resul)
