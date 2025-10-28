'''
¿Qué es Matplotlib?
Matplotlib es una biblioteca de visualización de datos en Python que permite crear gráficos estáticos, animados e interactivos. Es compatible con una amplia gama de backends y plataformas, lo que la hace versátil para su uso en diferentes entornos de desarrollo. Utiliza un enfoque basado en scripts, lo que facilita la creación de gráficos de manera programática mediante la definición de figuras, ejes y elementos gráficos.

Matplotlib ofrece una API orientada a objetos (Object-Oriented API) que permite tener un control preciso sobre el diseño del gráfico. Esta API te brinda la capacidad de crear y manipular directamente objetos como figuras (Figure), ejes (Axes) y otros elementos gráficos, lo que proporciona una mayor flexibilidad y personalización en la creación de gráficos complejos.

Al utilizar la API orientada a objetos, puedes:

Crear múltiples figuras y subgráficos en disposiciones personalizadas.
Controlar la posición y tamaño de cada elemento gráfico.
Personalizar propiedades detalladas como colores, estilos de línea, fuentes y más.
Interactuar con los elementos del gráfico para actualizaciones dinámicas.
Matplotlib se integra de manera eficiente con otras bibliotecas del ecosistema científico de Python, como NumPy y Pandas, lo que facilita la manipulación y visualización de conjuntos de datos complejos. Esta interoperabilidad permite a los usuarios transformar y representar datos de manera sencilla, aprovechando las capacidades de estas bibliotecas para el cálculo numérico y el análisis de datos.

La biblioteca es extensible, lo que significa que los desarrolladores pueden crear nuevos tipos de gráficos y personalizar los existentes utilizando el sistema de plugins de Matplotlib. Además, ofrece soporte completo para el etiquetado, la anotación y la creación de leyendas, lo que enriquece la interpretación visual de los datos.
'''

import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def separator_line():
    print('\n' + '-' * 50 + '\n')

print(matplotlib.__version__)

separator_line()

# Crear un array de datos
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Generar el gráfico
plt.plot(x, y)
plt.title('Gráfico de seno')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()

separator_line()


# Crear un DataFrame de ejemplo
data = {'Categoria': ['A', 'B', 'C'], 'Valores': [10, 20, 15]}
df = pd.DataFrame(data)

# Generar el gráfico de barras
df.plot(kind='bar', x='Categoria', y='Valores', legend=False)
plt.title('Gráfico de barras')
plt.ylabel('Valores')
plt.show()

separator_line()

fig, ax = plt.subplots()
x = [0, 1, 2, 3, 4]
y = [10, 15, 13, 18, 16]
ax.plot(x, y, label='Datos de ejemplo')

ax.set_title('Título del gráfico')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')

ax.legend()

plt.show()

separator_line()
