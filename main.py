
from validaciones import validar_cantidad_alumnos, validar_nota, validar_nombre
from procesamiento import (
    calcular_promedios,
    mostrar_listado,
    mostrar_estadisticas,
    ordenar_burbuja,
    juegos_con_nombre,
    buscar_alumno,
)

def main():
    nombres = []
    parcial1 = []
    parcial2 = []
    promedios = []
    datos_cargados = False

    continuar = True
    while continuar == True:
        print("\n===== NOTAFACIL =====")
        print("1. Cargar alumnos")
        print("2. Mostrar listado")
        print("3. Mostrar estadisticas")
        print("4. Ver ranking (ordenado)")
        print("5. Buscar alumno")
        print("6. Juegos con un nombre")
        print("0. Salir")

        opcion = input("Elija una opcion: ")

        match opcion:
            case "1":
                cant = validar_cantidad_alumnos()
                nombres = []
                parcial1 = []
                parcial2 = []
                
                for i in range(cant):
                    print("\n--- Carga del alumno", i + 1, "---")
                    nom = validar_nombre()
                    p1 = validar_nota("Ingrese nota del Parcial 1 (0-10): ")
                    p2 = validar_nota("Ingrese nota del Parcial 2 (0-10): ")
                    
                    nombres = nombres + [nom]
                    parcial1 = parcial1 + [p1]
                    parcial2 = parcial2 + [p2]

                promedios = calcular_promedios(parcial1, parcial2)
                datos_cargados = True
                print("Alumnos cargados exitosamente.")

            case "2":
                if datos_cargados == False:
                    print("Atencion: Primero debe cargar los alumnos (Opcion 1).")
                else:
                    mostrar_listado(nombres, parcial1, parcial2, promedios)

            case "3":
                if datos_cargados == False:
                    print("Atencion: Primero debe cargar los alumnos (Opcion 1).")
                else:
                    mostrar_estadisticas(nombres, promedios)

            case "4":
                if datos_cargados == False:
                    print("Atencion: Primero debe cargar los alumnos (Opcion 1).")
                else:
                    ordenar_burbuja(nombres, parcial1, parcial2, promedios)
                    mostrar_listado(nombres, parcial1, parcial2, promedios)

            case "5":
                if datos_cargados == False:
                    print("Atencion: Primero debe cargar los alumnos (Opcion 1).")
                else:
                    buscar_alumno(nombres, parcial1, parcial2, promedios)

            case "6":
                if datos_cargados == False:
                    print("Atencion: Primero debe cargar los alumnos (Opcion 1).")
                else:
                    nom_juego = validar_nombre()
                    juegos_con_nombre(nom_juego)

            case "0":
                print("Gracias por usar NotaFacil. Saliendo del programa...")
                continuar = False

            case _:
                print("Opcion invalida. Por favor, elija una opcion del menu.")


if __name__ == "__main__":
    main()