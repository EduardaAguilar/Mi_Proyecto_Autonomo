# =====================================================
# Lógica de Programación
# Autónomo 2
# Proyecto: Juego del Ahorcado
# Autor: Eduarda Aguilar
# =====================================================

# -----------------------------
# Declaración e inicialización de variables
# -----------------------------

palabra = "BUCLE"
pista = "Estructura que permite repetir instrucciones mientras se cumpla una condicion."

intentos = 6
letras_correctas = 0

usadaB = False
usadaU = False
usadaC = False
usadaL = False
usadaE = False

# -----------------------------
# Bienvenida
# -----------------------------

print("========================================")
print("        JUEGO DEL AHORCADO")
print("========================================")
print()

nombre = input("Ingrese su nombre: ")

print()
print("Bienvenido", nombre)
print()

# -----------------------------
# Inicio del juego
# -----------------------------

while intentos > 0 and letras_correctas < 5:

    print("----------------------------------------")
    print("Jugador:", nombre)
    print("Pista:", pista)
    print("Palabra: _ _ _ _ _")
    print("Intentos restantes:", intentos)
    print()

    letra = input("Ingrese una letra: ").upper()

    correcta = False

    # Validación letra B

    if letra == "B" and usadaB == False:
        usadaB = True
        letras_correctas = letras_correctas + 1
        correcta = True

    # Validación letra U

    if letra == "U" and usadaU == False:
        usadaU = True
        letras_correctas = letras_correctas + 1
        correcta = True

    # Validación letra C

    if letra == "C" and usadaC == False:
        usadaC = True
        letras_correctas = letras_correctas + 1
        correcta = True

    # Validación letra L

    if letra == "L" and usadaL == False:
        usadaL = True
        letras_correctas = letras_correctas + 1
        correcta = True

    # Validación letra E

    if letra == "E" and usadaE == False:
        usadaE = True
        letras_correctas = letras_correctas + 1
        correcta = True

    # Resultado de la validación

    if correcta:

        print()
        print("¡Letra correcta!")

    else:

        print()
        print("Letra incorrecta o ya utilizada.")
        intentos = intentos - 1

    print()

# -----------------------------
# Resultado final
# -----------------------------

if letras_correctas == 5:

    print("========================================")
    print("FELICIDADES", nombre)
    print("HAS GANADO EL JUEGO")
    print("La palabra era:", palabra)
    print("========================================")

else:

    print("========================================")
    print("HAS PERDIDO", nombre)
    print("La palabra correcta era:", palabra)
    print("========================================")

print()
print("Gracias por jugar.")
print("Fin del programa.")