print("ingrese dos numeros enteros para imprimir:")
dividendo = int(input("Dividendo:"))
divisor = int(input("Divisor:"))
cociente = dividendo / divisor
residuo = dividendo % divisor
if (residuo == 0) and (divisor * cociente == dividendo):
    print("la division es exacta.")
    print("cociente:" + str(cociente))
    print("residuo:" + str(residuo))
else:
    print("la division no es exacta.")
    print("cociente:" + str(cociente))
    print("residuo:" + str(residuo))
