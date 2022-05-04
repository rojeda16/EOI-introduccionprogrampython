num1= input("ingresa primer numero")
while(not num1.isdigit()):
    num1 = input("ingresa primer numero correctamenta sin letras: ")
num1 = int(num1)

num2= input("ingresa segundo numero")
while(not num2.isdigit()):
    num2= input("ingresa segundo numero correctamenta sin letras: ")
num2 = int(num2)


print (num1 + num2)

print (num1 - num2)

print (num1 * num2)

if (num2 == 0):
    print("no se puede dividir entre cero")
else :
    print(num1 / num2)
