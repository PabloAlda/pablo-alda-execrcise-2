# Definir una lista para almacenar la información de los jugadores
jugadores = []

# Solicitar al usuario la información de cada jugador
num_jugadores = int(input("Ingrese el número de jugadores: "))

for i in range(num_jugadores):
    print(f"\nIngrese la información del jugador {i + 1}:")
    nombre = input("Nombre del jugador: ")
    altura = float(input("Altura en centímetros: "))
    peso = float(input("Peso en kilogramos: "))
    promedio_ppp = float(input("Promedio de puntos por partido: "))
    asistencias = float(input("Promedio de asistencias por partido: "))
    rebotes = float(input("Promedio de rebotes por partido: "))

    # Almacenar la información del jugador en un diccionario
    jugador = {
        "Nombre": nombre,
        "Altura": altura,
        "Peso": peso,
        "PromedioPPP": promedio_ppp,
        "Asistencias": asistencias,
        "Rebotes": rebotes
    }

    # Agregar el jugador a la lista
    jugadores.append(jugador)

# Definir criterios para clasificar a los jugadores en posiciones
def clasificar_posicion(jugador):
    if (jugador["Altura"] > 210 and jugador["Peso"] > 110 and jugador["Rebotes"] > 15):
        return "Super-Pívot"
    elif (jugador["Asistencias"] > 20):
        return "Pulpo"
    elif (jugador["PromedioPPP"] > 30 and jugador["Asistencias"] < 3 and jugador["Rebotes"] < 3 ):
        return "Francotirador"
    elif (jugador["Altura"] > 200 and jugador["Peso"] > 90 and jugador["PromedioPPP"] > 15) or (jugador["Asistencias"] > 5 and jugador["Rebotes"] > 10):
        return "Pívot"
    elif (jugador["Altura"] > 190 and jugador["PromedioPPP"] > 10) or (jugador["Asistencias"] > 3 and jugador["Rebotes"] > 8):
        return "Ala-Pívot"
    elif (jugador["Altura"] > 180 and jugador["PromedioPPP"] > 8) or (jugador["Asistencias"] > 2 and jugador["Rebotes"] > 5):
        return "Alero"
    elif (jugador["PromedioPPP"] > 12) or (jugador["Asistencias"] > 4 and jugador["Rebotes"] > 3):
        return "Escolta"
    else:
        return "Base"

# Clasificar a cada jugador y mostrar la posición
print("\nPosiciones de los jugadores:")
for jugador in jugadores:
    posicion = clasificar_posicion(jugador)
    print(f"{jugador['Nombre']}: {posicion}")
