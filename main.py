'''
Calculadora de Estadisticas Personales
Autor: Javier Berrone
'''

from estadisticas import calcular_estadisticas
from utils import obtener_datos, mostrar_menu, guardar_resultados

def main():
    print("Bienvenido a la Calculadora de Estadísticas Personales")  # Mensaje de bienvenida

    datos = obtener_datos()  # Obtiene los datos del usuario
    
    while True:  # Bucle para mostrar el menú y procesar opciones
        opcion = mostrar_menu()  # Muestra el menú y obtiene la opción del usuario
        if opcion == '1':
            # Un junior podría no guardar los resultados en una variable
            # y simplemente imprimirlos directamente.
            resultado = calcular_estadisticas(datos)  # Calcula las estadísticas
            print("\nResultados:")
            for clave, valor in resultado.items():
                print(f"- {clave}: {valor}")
        elif opcion == '2':
            # Para arreglar el bug de guardar sin calcular, un junior
            # podría simplemente volver a calcular justo antes de guardar.
            # No es lo más eficiente, pero funciona.
            print("Calculando de nuevo para guardar...")
            resultado = calcular_estadisticas(datos)
            guardar_resultados(datos, resultado)
            print("Resultados guardados en 'calculadora_estadisticas/data/resultados.txt'.")
        elif opcion == '3':
            print("Gracias por usar la Calculadora de Estadísticas Personales")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


    
if __name__ == "__main__":
    main()  # Llama a la función principal para iniciar el programa
