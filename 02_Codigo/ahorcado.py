print("================================")
print("   JUEGO DEL AHORCADO")
print("================================")

nombre = input("Ingrese su nombre: ")

palabra = "PYTHON"

intentos = 6
letras_correctas = 0

print()
print("Bienvenido", nombre)
print()

while intentos > 0 and letras_correctas < 6:

    print("------------------------")
    print("Intentos restantes:", intentos)

    letra = input("Ingrese una letra: ")

    correcta = (
        letra == "P"
        or letra == "Y"
        or letra == "T"
        or letra == "H"
        or letra == "O"
        or letra == "N"
    )

    if correcta:

        print("Letra correcta")

        letras_correctas += 1

    else:

        print("Letra incorrecta")

        intentos -= 1


print()

if letras_correctas == 6:

    print("FELICIDADES", nombre)
    print("Has ganado")

else:

    print("Has perdido")
    print("La palabra era:", palabra)

print()
print("Fin del programa")