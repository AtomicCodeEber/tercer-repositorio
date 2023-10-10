# Comando Break

print("While con la sentencia Break \n")

contador=0

while contador<10:
    contador+=1
    if contador==5:
        break
    print(("El valor del contador", contador))

print("End of the problem.")

# Comando Continue

print("While con la sentencia Continue \n")

marker=0

while marker<10:
    marker+=1
    if marker==5:
        continue
    print("El valor de la sentencia es: ",marker)