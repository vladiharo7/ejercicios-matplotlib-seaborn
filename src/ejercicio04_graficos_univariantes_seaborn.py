'''
Utilizando la biblioteca Seaborn, crea un histograma para visualizar la distribución de la variable tip del conjunto de datos tips. 
Personaliza el histograma con los siguientes requisitos adicionales para hacerlo único.

Variable a graficar: Utiliza la variable tip.
Número de bins: Configura el histograma con 40 bins.
Visualización de densidad: Muestra la densidad en lugar de la frecuencia.
KDE: Superpón una curva KDE de color azul (color='blue').
Estilo general: Configura el estilo del gráfico con sns.set_style('darkgrid').
Etiquetas y título: Personaliza las etiquetas de los ejes y añade un título relevante para el gráfico.
'''

import seaborn as sns
import matplotlib.pyplot as plt

# 1. Configurar el estilo general del gráfico
sns.set_style('darkgrid')

# 2. Cargar el conjunto de datos de ejemplo 'tips'
tips = sns.load_dataset("tips")

# 3. Crear una figura de Matplotlib para mejor control
plt.figure(figsize=(10, 6))


# 4. Crear el histograma (histplot)
# Esta función combina todos los requisitos
ax = sns.histplot(
    data=tips,          # Usamos el dataframe 'tips'
    x='tip',            # Variable a graficar: tip
    bins=40,            # Número de bins: 40
    stat='density',     # Visualización de densidad (en lugar de 'count')
    kde=True,           # Superponer la curva KDE

    # Personalización del color:
    # 'color' define el color de las barras (lo ponemos gris para que el KDE resalte)
    color='lightgrey',

    # 'line_kws' pasa argumentos al 'lineplot' de Matplotlib que dibuja el KDE
    line_kws={
        'color': 'blue',  # Color de la línea KDE: azul
        'lw': 2.5         # Grosor de la línea
    }
)

# 5. Personalizar etiquetas y título
ax.set_title('Distribución de Densidad de las Propinas (Dataset "tips")', fontsize=16)
ax.set_xlabel('Monto de la Propina ($)', fontsize=12)
ax.set_ylabel('Densidad', fontsize=12)

# 6. Mostrar el gráfico
plt.show()
