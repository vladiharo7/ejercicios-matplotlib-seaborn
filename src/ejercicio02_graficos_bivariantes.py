'''
1.- Generación de los datos:

Crea dos conjuntos de datos con numpy. El primer conjunto x contendrá 100 valores aleatorios entre 0 y 50, y el segundo conjunto y tendrá una relación lineal con x (por ejemplo, y = 2.5 * x + ruido, donde el ruido es una pequeña variación aleatoria para simular datos reales). Se podría ver así:
x = rng.uniform(0, 50, 100)
ruido = rng.normal(0, 10, 100)
y = 2.5 * x + ruido
2.- Calcular la línea de regresión:

Utiliza numpy.polyfit para calcular la línea de regresión lineal que mejor se ajuste a los datos.
3.- Configuración del gráfico de dispersión:

Usa plt.scatter() para crear el gráfico de dispersión.
Configura el color de los puntos a púrpura (purple) y ajusta el tamaño de los puntos a 50 para mejorar la visualización.
Añade una línea de regresión con plt.plot() en color verde (green).
Incluye una cuadrícula para mejorar la interpretación del gráfico.
4.- Etiquetas y título:

Añade un título descriptivo para el gráfico, además de etiquetas para los ejes X e Y.
5.- Visualización:

Muestra el gráfico utilizando plt.show().
'''

import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# x: 100 valores aleatorios entre 0 y 50
x = rng.uniform(0, 50, 100)

# ruido: 100 valores aleatorios de una distribución normal (media 0, desv. est. 10)
ruido = rng.normal(0, 10, 100)

# y: relación lineal con x más el ruido
y = 2.5 * x + ruido

# --- 2. Calcular la línea de regresión ---

# np.polyfit(x, y, 1) calcula los coeficientes de un polinomio de grado 1 (una línea)
# Devuelve un array [pendiente, ordenada_en_el_origen]
pendiente, ordenada_origen = np.polyfit(x, y, 1)

# Creamos los valores 'y' para la línea de regresión
# y = (pendiente * x) + ordenada_en_el_origen
# Usamos los valores mínimo y máximo de x para dibujar la línea
x_linea = np.array([x.min(), x.max()])
y_linea = pendiente * x_linea + ordenada_origen

print(f"La línea de regresión calculada es: y = {pendiente:.4f}x + {ordenada_origen:.4f}")

# --- 3. Configuración del gráfico de dispersión ---

# Creamos la figura y los ejes
plt.figure(figsize=(10, 6))

# Gráfico de dispersión
plt.scatter(x, y, color='purple', s=50, label='Datos Observados')

# Añadir la línea de regresión
# Usamos una f-string para mostrar la ecuación en la leyenda
label_linea = f'Línea de Regresión (y={pendiente:.2f}x + {ordenada_origen:.2f})'
plt.plot(x_linea, y_linea, color='green', linewidth=2, label=label_linea)

# Incluir cuadrícula
plt.grid(True)

# --- 4. Etiquetas y título ---

plt.title('Gráfico de Dispersión con Regresión Lineal')
plt.xlabel('Variable Independiente (x)')
plt.ylabel('Variable Dependiente (y)')

# Añadimos una leyenda para identificar los puntos y la línea
plt.legend()

# --- 5. Visualización ---

# Muestra el gráfico
plt.show()
