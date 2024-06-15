# Se importa el modulo random
import random

# Función para elegir número random
def numeroRandom (max):
    return random.randint(1, max)

# Función para adivinar número
def adivinarNum (numero_aleatorio, maximo, dificultad):
    flag = True
    intentos = 0
    while flag:
        # Controlar que el usuario solo pase números enteros
        try:
            numero_adivinado = int(input(f"Adivine un número entre el 1 - {maximo}:\n>"))
        except:
            print("Solo se permiten números enteros.\n")
            continue

        # Controlar que el número este en el rango de dificultad
        if numero_adivinado < 1 or numero_adivinado > maximo:
            print("Número no válido, intente de nuevo\n")
            continue

        
        # Verifica que el numero ingresado sea igual al numero aleatorio
        intentos += 1
        if numero_adivinado == numero_aleatorio :
            flag = False
        else :
            if numero_adivinado < numero_aleatorio :
                print("Más alto")
            else:
                print("Mas bajo")
    return f"{intentos} Intentos - Dificultad {dificultad}"

# Función para elegir dificultad
def elegirDificultad ():
    while True:
        print("NIVEL 1 => 1 - 10 (Facil)\nNIVEL 2 => 1 - 100 (Medio)\nNIVEL 3 => 1 - 1000 (Dificil)\nNIVEL 4 => 1 - 10000 (Experto)")

        # Controlar que el usuario solo pase números enteros
        try:
            dificultad = int(input("> "))
        except:
            print("Solo se permiten números enteros.\n")
            continue

        # Retornar dificultad elegida
        match dificultad:
            case 1:
                return 10, "Facil"
            case 2:
                return 100, "Medio"
            case 3:
                return 1000, "Dificil"
            case 4:
                return 10000, "Experto"
            case _:
                print("Elegir una dificultad válida\n")

# Función para mostrar tabla de intentos
def tablaIntentos (intento, lista = []):
    # Se agrega y ordena los intentos de menor a mayor
    lista.append(intento)
    lista.sort()
    
    print("Tabla de intentos")
    for int in lista:
        print(int)

# Función para iniciar el juego
def iniciarJuego ():
    flag = True
    print("JUEGO DE ADIVINAR EL NÚMERO")
    print("---------------------------")
    print("El objetivo es adivinar el número secreto con la menor cantidad de intentos.")
    print("---------------------------")
    while flag:
        print("Elija la dificultad que desea jugar:\n")
        maximo, dificultad = elegirDificultad()
        numero_aleatorio = numeroRandom(maximo)
        intentos = adivinarNum(numero_aleatorio, maximo, dificultad)
        print("---------------------------")
        tablaIntentos(intentos)
        print("---------------------------")
        continuar = input("Desea volver a intentar?\n(Escriba ('n'/'no') para salir del juego, ó presione cualquier otra tecla para continuar):\n> ")
        if continuar.lower() == "n" or continuar.lower() == "no" :
            flag = False
            print("Gracias por jugar")

iniciarJuego()
