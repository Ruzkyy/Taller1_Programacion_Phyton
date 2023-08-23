caracter = input("ingrese un caracter: ")
asciivalor = ord(caracter)
if (asciivalor >= 49) and (asciivalor <= 57):
    print("Es un numero")
elif (asciivalor >= 65) and (asciivalor <= 90):
    print("Es una letra mayuscula")
elif (asciivalor >= 97) and (asciivalor <= 122):
    print("Es una letra miniscula")
else:
    print("No es ni una letra ni un numero")
