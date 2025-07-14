'''
Funciones auxiliares: entrada de datos, validacion y guardado en archivo
'''



def obtener_datos():
    """
    Solicita al usuario que ingrese una lista de números separados por comas.

    Retorna:
        list: Lista de números (float) ingresados por el usuario.
    """
    while True:  # Esto repite hasta que el usuario ingrese bien los datos
        entrada = input("Ingrese una lista de números separados por comas: ")  # Pide los números al usuario
        numeros = entrada.split(',')  # Separa los números usando la coma
        try:
            lista_numeros = []  # Creo una lista vacía para guardar los números
            for num in numeros:  # Recorre cada número que el usuario puso
                numero = float(num.strip())  # Quita espacios y convierte a float
                lista_numeros.append(numero)  # Agrega el número a la lista
            return lista_numeros  # Devuelve la lista si todo salió bien
        except ValueError:  # Si hay un error al convertir a float
            print("Entrada no válida. Por favor, ingrese números válidos.")  # Muestra un mensaje de error

def mostrar_menu():
    """
    Muestra el menú principal de opciones al usuario y devuelve la opción elegida.
    """
    print("""
          Seleccione una opción:
            1. Calcular estadísticas descriptivas
            2. Guardar resultados en un archivo
            3. Salir
          """)  # Muestra el menú en pantalla
    return input("Ingrese su opción: ")  # Pide al usuario que ingrese una opción y la devuelve 



def guardar_resultados(lista_numeros, estadisticas):
    '''
    Guarda los datos ingresados por el usuario en un archivo de texto.
    '''
    # Usamos 'a' para que los resultados se agreguen al final del archivo
    with open('data/resultados.txt', 'a') as archivo:
        # Convierte la lista de números a un string separado por comas
        datos_str = ','.join(map(str, lista_numeros))
        archivo.write(f"Datos: {datos_str}\n")
        
        archivo.write("Resultados:\n")
        for clave, valor in estadisticas.items():
            archivo.write(f"- {clave}: {valor}\n")
        archivo.write("---\n") # Separador para la próxima vez
