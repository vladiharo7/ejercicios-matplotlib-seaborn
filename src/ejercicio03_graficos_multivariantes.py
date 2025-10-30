'''
Crea un gráfico de dispersión multivariante utilizando Matplotlib para visualizar la relación entre cuatro variables. Genera un conjunto de datos aleatorios para las variables X, Y, color y tamaño. El gráfico debe seguir las siguientes especificaciones:

1.- Generación de datos:

Usa numpy para generar 200 puntos de datos para las variables X e Y con valores aleatorios entre 0 y 10.
La tercera variable debe mapearse a colores utilizando valores aleatorios entre 0 y 100.
La cuarta variable debe ser utilizada para el tamaño de los puntos, con valores aleatorios multiplicados por 200 para que los tamaños sean visibles.
2.- Configuración del gráfico de dispersión:

Usa plt.scatter() para crear el gráfico de dispersión.
Configura el color de los puntos mapeado a la tercera variable utilizando la paleta de colores plasma.
Ajusta el tamaño de los puntos mapeado a la cuarta variable y establece una transparencia (alpha) de 0.6 para mejorar la visibilidad.
3.- Etiquetas y título:

Añade un título descriptivo al gráfico, y etiquetas para los ejes X e Y.
4.- Barra de colores:

Añade una barra de colores que represente la escala de la tercera variable.
5.- Visualización:

Muestra el gráfico.
'''

import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# 1.- Generación de datos:
x = rng.uniform(0, 10, 200)
y = rng.uniform(0, 10, 200)

colors = rng.uniform(0, 10, 200)

sizes = 200 * rng.random(200)

# 2.- Configuración del gráfico de dispersión:
plt.figure(figsize=(10, 6))
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, cmap='plasma', edgecolors='w', linewidth=0.5)

# 3.- Etiquetas y título:
plt.xlabel('Variable X')
plt.ylabel('Variable Y')
plt.title('Gráfico de dispersión multivariante')

plt.colorbar(scatter, label='Escala de colores')
plt.show()
