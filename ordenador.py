print("Ingrese 4 numero:")
numero1 = int(input("Numero 1:"))
numero2 = int(input("Numero 2:"))
numero3 = int(input("Numero 3:"))
numero4 = int(input("Numero 4:"))
if numero1 >= numero2 and numero1 >= numero3 and numero1 >= numero4 :
    mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3 and numero2 >= numero4 :
    mayor = numero2
elif numero3 >= numero1 and numero3 >= numero2 and numero3 >= numero4 :
    mayor = numero3
else:
    mayor = numero4
if numero1 <= numero2 and numero1 <= numero3 and numero1 <= numero4 :
    menor = numero1
elif numero2 <= numero1 and numero2 <= numero3 and numero2 <= numero4 :
    menor = numero2
elif numero3 <= numero1 and numero3 <= numero2 and numero3 <= numero4 :
    menor = numero3
else:
    menor = numero4
intermedios = [numero1, numero2, numero3, numero4]
intermedios.remove(mayor)
intermedios.remove(menor)
inter1, inter2 = intermedios
if inter1 >= inter2 :
    mayorinte = inter1
    menorinte = inter2
elif inter2 >= inter1 :
    mayorinte = inter2
    menorinte = inter1
print(menor, menorinte, mayorinte, mayor)