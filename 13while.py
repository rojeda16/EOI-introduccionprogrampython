print("antes de while")

valor = 0
while (valor<5):
    valor+=1
    #print(f"valor actual: {valor}")
    if (valor == 3):
        continue
    print(f"valor actual: {valor}")
print ("despues de while")


print("antes de while")

valor = 0
while (valor<5):
    valor+=1
    #print(f"valor actual: {valor}")
    #if (valor == 3):
        #continue
    if (valor != 3):
        print(f"valor actual: {valor}")
print ("despues de while")




print("antes de while")

valor = 0
while (valor<5):
    valor+=1
    #print(f"valor actual: {valor}")
    if (valor > 3):
        #continue
        break
    print(f"valor actual: {valor}")
print ("despues de while")


