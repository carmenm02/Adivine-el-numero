import random 
numero = random.randint(0, 100)
intento = int(input("Introduzca el numero: "))
numero_intentos = 1
while intento != numero :
    numero_intentos += 1
    intento = int(input("Introduzca el numero: "))
    if intento <= numero :
        print("Demasiado pequeño")
    elif numero >= numero :
        print("Demasiado grande")
if intento == numero :
    print("¡Has ganado!")

print("Cantidad de intentos: " + str(numero_intentos))