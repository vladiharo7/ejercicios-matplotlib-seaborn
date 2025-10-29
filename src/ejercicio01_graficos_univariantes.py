'''
Crea un histograma utilizando Matplotlib para visualizar la distribución de un conjunto de datos generado aleatoriamente. Debes seguir las siguientes especificaciones:

1.- Generación de datos:

Usa numpy para crear un conjunto de 1500 datos con distribución normal (media=5, desviación estándar=2).
2.- Configuración del histograma:

Utiliza plt.hist() para crear el histograma.
Establece el número de intervalos (bins) en 40.
Configura el color de las barras a verde con una transparencia (alpha) de 0.5.
Añade bordes rojos a las barras para mejorar la claridad visual.
3.- Añadir información al gráfico:

Incluye un título descriptivo, y etiquetas para los ejes x e y.
4.- Visualización:

Muestra el gráfico.
'''

import matplotlib.pyplot as plt
import numpy as np

# Crear un generador de números aleatorios con una semilla específica
rng = np.random.default_rng(seed=42)

# Generar datos aleatorios utilizando el generador
data = rng.normal(5, 2, 1500)

# 2. Configuración del histograma
plt.style.use('seaborn-v0_8')  # Estilo visual limpio

plt.hist(data, bins=40, color='green', alpha=0.5, edgecolor='red')

# 3. Información del gráfico
plt.title('Distribución Normal de Datos Generados Aleatoriamente (μ=5, σ=2)')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')

# 4. Visualización
plt.tight_layout()
plt.show()
