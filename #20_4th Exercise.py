
print("======================================")
print("             Calculadora")
print("======================================")

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. División entera")
print("6. Exponente")
print("7. Módulo o resto")
print("\n")

operation=int(input("Selecciona la operación a realizar: "))

if operation==1:
    print("=====Suma=====")
    number=float(input("Ingrese el sumando:"))
    number+=float(input("Ingrese el segundo sumando: "))
    print("El resultado de la operación es:",number)
elif operation==2:
    print("=====Resta=====")
    number=float(input("Ingrese el minuendo:"))
    number-=float(input("Ingrese el sustraendo: "))
    print("El resultado de la operación es:",number)
elif operation==3:
    print("=====Multiplicación=====")
    number=float(input("Ingrese el primer factor: "))
    number*=float(input("Ingrese el segundo factor: "))
    print("El resultado de la operación es:",number)
elif operation==4:
    print("=====División=====")
    number=float(input("Ingrese el dividendo:"))
    number/=float(input("Ingrese el segundo divisor: "))
    print("El resultado de la operación es:",round(number, 3))
elif operation==5:
    print("=====División Entera=====")
    number=float(input("Ingrese el dividendo:"))
    number//=float(input("Ingrese el segundo divisor: "))
    print("El resultado de la operación es:",number)
elif operation==6:
    print("=====Potencia=====")
    number=float(input("Ingrese la base:"))
    number**=float(input("Ingrese el exponente de la base: "))
    print("El resultado de la operación es:",number)
elif operation==7:
    print("=====Módulo=====")
    number=float(input("Ingrese el dividendo:"))
    number%=float(input("Ingrese el divisor: "))
    print("El resultado de la operación es:",number)
else:
    print("Término inadmisible. Escoja otra opación.")