'''
Utilizando Seaborn en Python, crea un script que genere un gráfico de barras (barplot) con datos ficticios. 
El gráfico debe cumplir los siguientes requisitos:

Crea un DataFrame con datos ficticios:
El DataFrame debe tener dos columnas:
Categoría, que contiene las categorías A, B, C, D.
Valor, que contiene los valores numéricos 10, 15, 7, 12.
Aplica el tema predefinido whitegrid al gráfico.
Utiliza la paleta de colores pastel para las barras.
Crea un gráfico de barras:
Usa la función sns.barplot() para graficar los datos del DataFrame:
Eje x: la columna Categoría.
Eje y: la columna Valor.
Asigna la columna Categoría al parámetro hue para garantizar compatibilidad con futuras versiones de Seaborn.
Establece la paleta de colores pastel mediante el argumento palette.
Personaliza el título del gráfico:
El título debe ser: Gráfico de barras personalizado.
Debe tener:
Tamaño de fuente de 16.
Color azul.
Negrita (bold).
Personaliza las etiquetas de los ejes:
Cambia la etiqueta del eje x a Categorías y la del eje y a Valores.
Ambas etiquetas deben tener:
Tamaño de fuente de 12.
Color gris oscuro.
Elimina bordes específicos del gráfico:
Usa sns.despine() para eliminar los bordes izquierdo y derecho del gráfico.
Muestra el gráfico resultante.
'''


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Crear el DataFrame con datos ficticios
data = {
    'Categoría': ['A', 'B', 'C', 'D'],
    'Valor': [10, 15, 7, 12]
}
df = pd.DataFrame(data)

# 2. Aplicar el tema predefinido 'whitegrid'
sns.set_style('whitegrid')

# 3. Crear la figura y los ejes para mayor control
plt.figure(figsize=(8, 6))

# 4. Crear el gráfico de barras (barplot)
# Se utiliza 'errorbar=None' ya que 'barplot' por defecto muestra barras de error
# que no son necesarias con solo un valor por categoría.
ax = sns.barplot(
    data=df,
    x='Categoría',
    y='Valor',
    hue='Categoría',      # Asigna 'Categoría' al parámetro hue
    palette='pastel',     # Utiliza la paleta de colores 'pastel'
    errorbar=None         # Oculta las barras de error por defecto
)

# 5. Personalizar el título del gráfico
ax.set_title(
    'Gráfico de barras personalizado',
    fontsize=16,
    color='blue',
    fontweight='bold'
)

# 6. Personalizar las etiquetas de los ejes
# Eje X
ax.set_xlabel(
    'Categorías',
    fontsize=12,
    color='dimgray' # Gris oscuro
)

# Eje Y
ax.set_ylabel(
    'Valores',
    fontsize=12,
    color='dimgray' # Gris oscuro
)

# Ocultar la leyenda redundante generada por el parámetro hue
if ax.legend_ is not None:
    ax.legend_.remove()

# 7. Eliminar bordes específicos del gráfico
# Por defecto, despine elimina los bordes superior y derecho.
# Para eliminar el izquierdo y el derecho, especificamos:
sns.despine(left=True, right=True)

# 8. Muestra el gráfico resultante
plt.show()
