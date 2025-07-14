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

## 🛠️ Requisitos previos

- Python 3.8 o superior
- No se requieren librerías externas (solo módulos estándar)

---

## 🚀 Cómo ejecutar el proyecto

### 1. Clonar el repositorio o copiar el proyecto
```bash
git clone https://github.com/javi2481/calculadora_estadisticas.git
```

### 2. Crear y activar un entorno virtual (opcional pero recomendado)
```bash
python -m venv env_prog
env_prog\Scripts\activate     # En Windows
```

### 3. Crear la carpeta `data` si no existe
```bash
mkdir data
```

### 4. Ejecutar el programa
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

Ingrese una lista de números separados por comas (por ejemplo: 4, 6, 8, 10):
> 10, 20, 30, 40

Seleccione una opción:
1. Calcular estadísticas descriptivas
2. Guardar resultados en un archivo
3. Salir
> 1

Resultados:
- Media: 25.0
- Mediana: 25.0
- Moda: No hay moda única
- Maximo: 40.0
- Minimo: 10.0
- Suma total: 100.0
- Cantidad de valores: 4
- Desviacion estandar: 12.91
- Varianza: 166.67
```



---

## 📄 Ejemplo de archivo de resultados (`data/resultados.txt`)

Los resultados se guardan al final del archivo cada vez que se usa la opción 2.

```
Datos: 10.0,20.0,30.0,40.0
Resultados:
- Media: 25.0
- Mediana: 25.0
- Moda: No hay moda única
- Maximo: 40.0
- Minimo: 10.0
- Suma total: 100.0
- Cantidad de valores: 4
- Desviacion estandar: 12.91
- Varianza: 166.67
---
Datos: 1.0,2.0,3.0
Resultados:
- Media: 2.0
- Mediana: 2.0
- Moda: No hay moda única
- Maximo: 3.0
- Minimo: 1.0
- Suma total: 6.0
- Cantidad de valores: 3
- Desviacion estandar: 1.0
- Varianza: 1.0
---
```



---

## 📌 Autor

Javier Berrone – Junio 2025
