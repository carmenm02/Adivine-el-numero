import random 
numero = random.randint(0, 100)
print(numero)
intento = int(input("Adivina el numero"))
numero_intentos = 1
while intento != numero :
    if intento <= numero :
        print("Demasiado pequeño")
        numero_intentos += 1
    elif numero >= numero :
        print("Demasiado grande")
        numero_intentos += 1
if intento == numero :
    print("¡Has ganado!")
print("Cantidad de intentos: " + str(numero_intentos))
