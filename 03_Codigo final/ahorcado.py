# ===========================================================
# UNIVERSIDAD INTERNACIONAL DEL ECUADOR
# Asignatura: Lógica de Programación
# Aprendizaje Autónomo 2
# Proyecto: Juego del Ahorcado
# Estudiante: Eduarda Aguilar

# Descripción:
# El presente programa implementa una versión básica del juego
# del ahorcado aplicando los conocimientos adquiridos sobre
# variables, operadores lógicos, estructuras condicionales y
# estructuras repetitivas. El objetivo es que el usuario adivine
# una palabra relacionada con los contenidos de la asignatura
# antes de agotar el número de intentos disponibles.
# ===========================================================

# -----------------------------------------------------------
# DECLARACIÓN E INICIALIZACIÓN DE VARIABLES
# -----------------------------------------------------------

# Se declara la variable que almacena la palabra secreta
# que el usuario deberá descubrir durante el juego.
palabra = "BUCLE"

# Se almacena una pista relacionada con la palabra
# para orientar al usuario durante la partida.
pista = "Estructura que permite repetir instrucciones mientras se cumpla una condicion."

# Se inicializa el contador de intentos permitidos.
# El jugador dispone de seis oportunidades para adivinar
# correctamente la palabra.
intentos = 6

# Se inicializa el contador de letras correctas encontradas.
# Esta variable permitirá determinar cuándo el usuario
# ha completado la palabra.
letras_correctas = 0

# Se utilizan variables booleanas para registrar si cada
# letra de la palabra ya fue descubierta previamente.
# Esto evita que una misma letra sea contabilizada
# más de una vez.

usadaB = False
usadaU = False
usadaC = False
usadaL = False
usadaE = False

# -----------------------------------------------------------
# PRESENTACIÓN DEL PROGRAMA
# -----------------------------------------------------------

# Se muestra un mensaje de bienvenida que identifica
# el nombre del juego.

print("========================================")
print("        JUEGO DEL AHORCADO")
print("========================================")

# Se solicita el nombre del jugador y se almacena
# en una variable de tipo cadena.

nombre = input("Ingrese su nombre: ")

# Se presenta un mensaje personalizado utilizando
# el nombre ingresado por el usuario.

print()
print("Bienvenido", nombre)
print()

# -----------------------------------------------------------
# INICIO DEL CICLO PRINCIPAL DEL JUEGO
# -----------------------------------------------------------

# Se implementa una estructura repetitiva while para
# mantener el juego activo mientras existan intentos
# disponibles y la palabra no haya sido completada.

while intentos > 0 and letras_correctas < 5:

    # Se presenta al usuario el estado actual del juego,
    # incluyendo la pista y la cantidad de intentos restantes.

    print("----------------------------------------")
    print("Jugador:", nombre)
    print("Pista:", pista)
    print("Palabra: _ _ _ _ _")
    print("Intentos restantes:", intentos)
    print()

    # Se solicita el ingreso de una letra.
    # El método upper() convierte automáticamente
    # la entrada a mayúscula para facilitar la validación.

    letra = input("Ingrese una letra: ").upper()

    # Se inicializa una variable lógica que permitirá
    # determinar si la letra ingresada es correcta.

    correcta = False

    # -------------------------------------------------------
    # VALIDACIÓN DE LA LETRA B
    # -------------------------------------------------------

    # Se verifica si la letra ingresada corresponde a la
    # letra B y además que no haya sido utilizada anteriormente.

    if letra == "B" and usadaB == False:

        # Se registra que la letra ya fue utilizada.
        usadaB = True

        # Se incrementa el contador de letras correctas.
        letras_correctas = letras_correctas + 1

        # Se indica que la validación fue correcta.
        correcta = True

    # -------------------------------------------------------
    # VALIDACIÓN DE LA LETRA U
    # -------------------------------------------------------

    if letra == "U" and usadaU == False:

        usadaU = True
        letras_correctas = letras_correctas + 1
        correcta = True

    # -------------------------------------------------------
    # VALIDACIÓN DE LA LETRA C
    # -------------------------------------------------------

    if letra == "C" and usadaC == False:

        usadaC = True
        letras_correctas = letras_correctas + 1
        correcta = True

    # -------------------------------------------------------
    # VALIDACIÓN DE LA LETRA L
    # -------------------------------------------------------

    if letra == "L" and usadaL == False:

        usadaL = True
        letras_correctas = letras_correctas + 1
        correcta = True

    # -------------------------------------------------------
    # VALIDACIÓN DE LA LETRA E
    # -------------------------------------------------------

    if letra == "E" and usadaE == False:

        usadaE = True
        letras_correctas = letras_correctas + 1
        correcta = True

    # -------------------------------------------------------
    # EVALUACIÓN DEL RESULTADO
    # -------------------------------------------------------

    # Si la variable correcta es verdadera, el programa
    # informa que la letra pertenece a la palabra.

    if correcta:

        print()
        print("¡Letra correcta!")

    # En caso contrario, la letra es incorrecta o ya fue
    # utilizada anteriormente, por lo que se descuenta
    # un intento al jugador.

    else:

        print()
        print("Letra incorrecta o ya utilizada.")

        intentos = intentos - 1

    print()

# -----------------------------------------------------------
# RESULTADO FINAL DEL JUEGO
# -----------------------------------------------------------

# Se verifica si el usuario logró descubrir todas las
# letras de la palabra antes de agotar sus intentos.

if letras_correctas == 5:

    print("========================================")
    print("FELICIDADES", nombre)
    print("HAS GANADO EL JUEGO")
    print("La palabra era:", palabra)
    print("========================================")

# Si no logró completar la palabra, el programa informa
# la derrota y muestra la respuesta correcta.

else:

    print("========================================")
    print("HAS PERDIDO", nombre)
    print("La palabra correcta era:", palabra)
    print("========================================")

# Finalmente se presenta un mensaje de despedida indicando
# la finalización de la ejecución del programa.

print()
print("Gracias por jugar.")
print("Fin del programa.")
