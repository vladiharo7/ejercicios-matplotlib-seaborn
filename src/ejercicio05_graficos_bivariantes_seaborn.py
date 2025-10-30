'''
Utilizando Seaborn, crea una visualización bivariante que analice la relación entre dos variables numéricas del conjunto de datos tips. 
Personaliza el gráfico según los siguientes requisitos:

Carga el conjunto de datos tips utilizando sns.load_dataset.
Configura el estilo del gráfico a  whitegrid.
Crea un gráfico de dispersión entre las variables total_bill y tip.
Usa una paleta personalizada con el parámetro palette configurado como coolwarm.
Diferencia los puntos en función del sexo con el parámetro hue='sex'.
Ajusta el nivel de transparencia de los puntos con alpha=0.6 para mejorar la visualización en datos densos.
Añade un título descriptivo y etiquetas claras para ambos ejes.
Superpón una línea de regresión utilizando sns.regplot() para observar tendencias entre las variables, ocultando los puntos de dispersión con scatter=False.
Muestra el gráfico combinando ambas visualizaciones en un solo espacio.
'''

import seaborn as sns
import matplotlib.pyplot as plt

# 1. Cargar el conjunto de datos tips
tips = sns.load_dataset("tips")

# 2. Configurar el estilo del gráfico a 'whitegrid'
sns.set_style('whitegrid')

# 3. Crear la figura y los ejes (el "lienzo")
# Es necesario crear los ejes (ax) primero para poder dibujar ambos gráficos
# uno encima del otro.
plt.figure(figsize=(11, 7))
ax = plt.gca() # Get Current Axes

# 4. Superponer la línea de regresión (Requisito 8 y 9)
# Dibujamos esto primero para que quede "debajo" de los puntos.
sns.regplot(
    data=tips,
    x='total_bill',
    y='tip',
    scatter=False,     # Oculta los puntos de dispersión de esta capa
    ax=ax,             # Especifica que debe dibujarse en nuestro lienzo (ax)
    color='black',     # Damos un color oscuro a la línea de tendencia
    line_kws={'linestyle': '--', 'lw': 2} # Estilo de línea punteada
)

# 5. Crear el gráfico de dispersión (Requisitos 3, 4, 5 y 6)
# Dibujamos los puntos encima de la línea de regresión.
sns.scatterplot(
    data=tips,
    x='total_bill',
    y='tip',
    palette='coolwarm',  # Paleta personalizada: coolwarm
    hue='sex',           # Diferenciar puntos por 'sex'
    alpha=0.6,           # Nivel de transparencia: 0.6
    ax=ax                # Especifica que debe dibujarse en el mismo lienzo (ax)
)

# 6. Añadir título y etiquetas (Requisito 7)
ax.set_title('Relación entre Factura Total y Propina, diferenciado por Sexo', fontsize=16)
ax.set_xlabel('Factura Total ($)', fontsize=12)
ax.set_ylabel('Propina Recibida ($)', fontsize=12)

# 7. Muestra el gráfico combinado
plt.legend(title='Sexo') # Mejora la leyenda
plt.show()
