num1=int(input("ingresa primer numero"))
num2=int(input("ingresa segundo numero"))
num3=int(input("ingresa tercer numero"))

if ( num1 >= num2 and num1 >= num3):
    print(num1, f"es el mayor ")

elif( num2 >= num3 and num2 >= num1):
    print (num2, f"es el mayor ")

else:
    print(num3, f"es el mayor ")
