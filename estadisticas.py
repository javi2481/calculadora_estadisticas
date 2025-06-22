import statistics as stats

def calcular_estadisticas(lista_numeros):
    """
    Calcula varias estadísticas descriptivas a partir de una lista de números.

    Parámetros:
        lista_numeros (list): Lista de valores numéricos (int o float).

    Retorna:
        dict: Un diccionario con las siguientes claves y valores:
            - 'Media': Media aritmética de los valores.
            - 'Mediana': Valor central de la lista ordenada.
            - 'Moda': Valor que más se repite en la lista.
            - 'Maximo': Valor máximo de la lista.
            - 'Minimo': Valor mínimo de la lista.
            - 'Suma total': Suma de todos los valores.
            - 'Cantidad de valores': Número de elementos en la lista.
            - 'Desviacion estandar': Desviación estándar de los valores (redondeada a 2 decimales).

    Manejo de errores:
        Si ocurre un error estadístico (por ejemplo, no hay moda), se imprime un mensaje.
        Si ocurre cualquier otro error, también se imprime un mensaje.

    Ejemplo de uso:
        calcular_estadisticas([1, 2, 2, 3, 4])
    """
    resultados = {}
    try:
        resultados['Media'] = stats.mean(lista_numeros)
        resultados['Mediana'] = stats.median(lista_numeros)
        resultados['Moda'] = stats.mode(lista_numeros)  
        resultados['Maximo'] = max(lista_numeros)
        resultados['Minimo'] = min(lista_numeros)   
        resultados['Suma total'] = sum(lista_numeros)
        resultados['Cantidad de valores'] = len(lista_numeros)
        resultados['Desviacion estandar'] = round(stats.stdev(lista_numeros), 2)
    except stats.StatisticsError as e:
        print(f"Error al calcular estadísticas: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return resultados

