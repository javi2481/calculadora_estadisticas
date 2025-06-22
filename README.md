# Calculadora de Estadísticas Personales

Este proyecto en Python permite al usuario ingresar una serie de números y calcular estadísticas básicas como:

- Media
- Mediana
- Moda
- Máximo y mínimo
- Suma total
- Cantidad de valores
- Desviación estándar
- Varianza

También ofrece la opción de guardar los resultados en un archivo de texto.

---

## 🚀 Cómo ejecutar el proyecto

### 1. Clonar el repositorio o copiar el proyecto
```bash
https://github.com/javi2481/calculadora_estadisticas.git
```

### 2. Crear y activar un entorno virtual (opcional pero recomendado)
```bash
python -m venv env_prog
.venv\Scripts\activate     # En Windows
```

### 3. Ejecutar el programa
```bash
python main.py
```

---

## 📁 Estructura del proyecto

```
calculadora_estadisticas/
├── main.py                # Programa principal
├── estadisticas.py        # Cálculo de estadísticas
├── utils.py               # Entrada de datos y utilidades
├── data/                  # Resultados guardados
├── docs/                  # PDF del trabajo final
├── README.md              # Este archivo
├── requirements.txt       # Dependencias (vacío)
```

---

## 🧪 Ejemplo de uso

```
Bienvenido a la Calculadora de Estadísticas Personales

Ingrese una lista de números separados por coma (por ejemplo: 4, 6, 8, 10):
> 10, 20, 30, 40

Seleccione una opción:
1. Calcular estadísticas
2. Guardar resultados en archivo
3. Salir
> 1

Resultados de estadísticas calculadas:
Media: 25.0
Mediana: 25.0
Moda: No hay moda o hay múltiples valores más frecuentes
Máximo: 40.0
Mínimo: 10.0
Suma total: 100.0
Cantidad de valores: 4
Desviación estándar: 12.91
Varianza: 166.67
```

---

## 📌 Autor

Javier Berrone – Junio 2025