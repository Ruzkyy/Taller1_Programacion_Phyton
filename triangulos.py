print("ingrese la medida de los lados de un triangulo:")
ladoA = float(input("Lado A:"))
ladoB = float(input("lado B:"))
ladoC = float(input("lado C:"))
if ladoC < (ladoA + ladoB) and ladoA < (ladoB + ladoC) and ladoB < (ladoC + ladoA):
    if ladoA == ladoB and ladoB == ladoC:
        print("Es un triangulo equilatero")
    elif ladoA == ladoB or ladoB == ladoC or ladoA == ladoC:
        print("Es un triangulo isoceles")
    else:
        print("Es un triangulo escaleno")
else:
    print("No es un triangulo valido")