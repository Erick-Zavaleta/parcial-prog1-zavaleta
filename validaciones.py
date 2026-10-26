
def validar_cantidad_alumnos():
    """Pide y valida que la cantidad de alumnos este entre 1 y 30."""
    valido = False
    while valido == False:
        entrada = input("Ingrese la cantidad de alumnos (1 a 30): ")
        
        es_numero = True
        if len(entrada) == 0:
            es_numero = False
        else:
            for i in range(len(entrada)):
                caracter = entrada[i]
                if "0" <= caracter <= "9":
                    pass
                else:
                    es_numero = False
                    break
        
        if es_numero == True:
            cantidad = int(entrada)
            if 1 <= cantidad <= 30:
                valido = True
            else:
                print("Error: La cantidad debe estar entre 1 y 30.")
        else:
            print("Error: Debe ingresar un numero entero valido.")
            
    return cantidad


def validar_nota(mensaje):
    """Pide y valida una nota entera entre 0 y 10."""
    valido = False
    while valido == False:
        entrada = input(mensaje)
        
        es_numero = True
        if len(entrada) == 0:
            es_numero = False
        else:
            for i in range(len(entrada)):
                caracter = entrada[i]
                if "0" <= caracter <= "9":
                    pass
                else:
                    es_numero = False
                    break
        
        if es_numero == True:
            nota = int(entrada)
            if 0 <= nota <= 10:
                valido = True
            else:
                print("Error: La nota debe estar entre 0 y 10.")
        else:
            print("Error: Debe ingresar un numero entero valido.")
            
    return nota


def validar_nombre():
    """Valida que el nombre tenga al menos 5 caracteres y solo contenga letras y espacios."""
    valido = False
    while valido == False:
        nombre = input("Ingrese el nombre del alumno: ")
        
        if len(nombre) < 5:
            print("Error: El nombre debe tener al menos 5 caracteres.")
        else:
            solo_letras_y_espacios = True
            for i in range(len(nombre)):
                caracter = nombre[i]
                es_minuscula = "a" <= caracter <= "z"
                es_mayuscula = "A" <= caracter <= "Z"
                es_espacio = caracter == " "
                
                if es_minuscula == True or es_mayuscula == True or es_espacio == True:
                    pass
                else:
                    solo_letras_y_espacios = False
                    break
            
            if solo_letras_y_espacios == True:
                valido = True
            else:
                print("Error: El nombre solo debe contener letras y espacios.")
            
    return nombre