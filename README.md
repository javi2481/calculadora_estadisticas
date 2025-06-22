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

## 📄 Ejemplo de archivo de resultados (`data/resultados.txt`)

```
Datos ingresados por el usuario: 2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0

Estadisticas calculadas:
Media: 5.5
Mediana: 5.5
Moda: 2.0
Maximo: 9.0
Minimo: 2.0
Suma total: 44.0
Cantidad de valores: 8
Desviacion estandar: 2.45
```

---

## 📌 Autor

Javier Berrone – Junio 2025