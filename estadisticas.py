import statistics as stats

def calcular_estadisticas(lista_numeros):
    """
    Calcula varias estadísticas descriptivas a partir de una lista de números.

    Parámetros:
        lista_numeros (list): Lista de valores numéricos (int o float).

    Retorna:
        dict: Un diccionario con las estadísticas calculadas.
    """
    resultados = {}
    try:
        resultados['Media'] = stats.mean(lista_numeros)
        resultados['Mediana'] = stats.median(lista_numeros)
        try:
            # La moda puede dar error si no hay una moda única
            resultados['Moda'] = stats.mode(lista_numeros)
        except stats.StatisticsError:
            resultados['Moda'] = "No hay moda única"
        resultados['Maximo'] = max(lista_numeros)
        resultados['Minimo'] = min(lista_numeros)
        resultados['Suma total'] = sum(lista_numeros)
        resultados['Cantidad de valores'] = len(lista_numeros)
        # La desviación estándar y la varianza necesitan al menos 2 datos
        if len(lista_numeros) > 1:
            resultados['Desviacion estandar'] = round(stats.stdev(lista_numeros), 2)
            resultados['Varianza'] = round(stats.variance(lista_numeros), 2)
        else:
            resultados['Desviacion estandar'] = "N/A (se necesita más de un dato)"
            resultados['Varianza'] = "N/A (se necesita más de un dato)"

    except Exception as e:
        print(f"Error inesperado al calcular estadísticas: {e}")
    
    return resultados
