
def calcular_promedios(parcial1, parcial2):
    """Calcula los promedios de los alumnos a partir de las listas de notas."""
    promedios = []
    for i in range(len(parcial1)):
        prom = (parcial1[i] + parcial2[i]) / 2
        promedios = promedios + [prom]
    return promedios


def mostrar_listado(nombres, parcial1, parcial2, promedios):
    """Muestra el listado completo de alumnos con sus notas y promedios."""
    if len(nombres) == 0:
        print("Atencion: No hay alumnos cargados en el sistema.")
    else:
        print("\n===== LISTADO DE ALUMNOS =====")
        for i in range(len(nombres)):
            print("Alumno:", nombres[i], "| Parcial 1:", parcial1[i], "| Parcial 2:", parcial2[i], "| Promedio:", promedios[i])


def mostrar_estadisticas(nombres, promedios):
    """Calcula y muestra estadisticas del curso sin usar funciones prohibidas."""
    if len(promedios) == 0:
        print("Atencion: No hay datos cargados para calcular estadisticas.")
    else:
        acumulador = 0
        for i in range(len(promedios)):
            acumulador = acumulador + promedios[i]
        promedio_general = acumulador / len(promedios)

        mejor_prom = promedios[0]
        peor_prom = promedios[0]
        nombre_mejor = nombres[0]
        nombre_peor = nombres[0]

        for i in range(len(promedios)):
            if promedios[i] > mejor_prom:
                mejor_prom = promedios[i]
                nombre_mejor = nombres[i]
            if promedios[i] < peor_prom:
                peor_prom = promedios[i]
                nombre_peor = nombres[i]

        cant_promociona = 0
        cant_aprueba = 0
        cant_desaprueba = 0

        for i in range(len(promedios)):
            if promedios[i] >= 6:
                cant_promociona = cant_promociona + 1
            else:
                if promedios[i] >= 4:
                    cant_aprueba = cant_aprueba + 1
                else:
                    cant_desaprueba = cant_desaprueba + 1

        print("\n===== ESTADISTICAS DEL CURSO =====")
        print("Promedio general del curso:", promedio_general)
        print("Mejor promedio:", nombre_mejor, "con", mejor_prom)
        print("Peor promedio:", nombre_peor, "con", peor_prom)
        print("Alumnos que promocionan (>= 6):", cant_promociona)
        print("Alumnos que aprueban (4 a 5.9):", cant_aprueba)
        print("Alumnos que desaprueban (< 4):", cant_desaprueba)


def ordenar_burbuja(nombres, parcial1, parcial2, promedios):
    """Ordena las listas paralelas de mayor a menor promedio usando el metodo burbuja."""
    n = len(promedios)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if promedios[j] < promedios[j + 1]:
                aux_prom = promedios[j]
                promedios[j] = promedios[j + 1]
                promedios[j + 1] = aux_prom

                aux_nom = nombres[j]
                nombres[j] = nombres[j + 1]
                nombres[j + 1] = aux_nom

                aux_p1 = parcial1[j]
                parcial1[j] = parcial1[j + 1]
                parcial1[j + 1] = aux_p1

                aux_p2 = parcial2[j]
                parcial2[j] = parcial2[j + 1]
                parcial2[j + 1] = aux_p2
                
    print("Ranking ordenado con exito por el metodo burbuja.")


def juegos_con_nombre(nombre):
    """Cuenta vocales y muestra el nombre invertido caracter por caracter."""
    vocales = 0
    for i in range(len(nombre)):
        c = nombre[i]
        es_vocal = (c == "a" or c == "e" or c == "i" or c == "o" or c == "u" or 
                    c == "A" or c == "E" or c == "I" or c == "O" or c == "U")
        if es_vocal == True:
            vocales = vocales + 1

    invertido = ""
    for i in range(len(nombre) - 1, -1, -1):
        invertido = invertido + nombre[i]

    print("\n--- JUEGOS CON NOMBRE ---")
    print("Nombre original:", nombre)
    print("Cantidad de vocales:", vocales)
    print("Nombre invertido:", invertido)


def buscar_alumno(nombres, parcial1, parcial2, promedios):
    """Busca un alumno por su nombre recorriendo la lista elemento por elemento."""
    if len(nombres) == 0:
        print("Atencion: No hay alumnos cargados para buscar.")
    else:
        buscado = input("Ingrese el nombre exacto del alumno a buscar: ")
        encontrado = False
        indice = -1

        for i in range(len(nombres)):
            if nombres[i] == buscado:
                encontrado = True
                indice = i
                break

        if encontrado == True:
            print("\nAlumno encontrado:")
            print("Nombre:", nombres[indice])
            print("Parcial 1:", parcial1[indice])
            print("Parcial 2:", parcial2[indice])
            print("Promedio:", promedios[indice])
        else:
            print("El alumno ingresado no existe en el registro.")