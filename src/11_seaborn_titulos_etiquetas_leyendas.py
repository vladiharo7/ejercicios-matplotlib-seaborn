import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
datos = sns.load_dataset('tips')

# Crear el gráfico
ax = sns.scatterplot(data=datos, x='total_bill', y='tip')

# Agregar un título
ax.set_title('Relación entre la cuenta total y la propina')

# Mostrar el gráfico
plt.show()



import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
datos = sns.load_dataset('tips')

# Crear un gráfico de distribución
g = sns.displot(data=datos, x='total_bill')

# Agregar un título a la figura
g.figure.suptitle('Distribución de la cuenta total')

# Ajustar los espacios para que el título no se superponga con el gráfico
g.figure.tight_layout()

# Mostrar el gráfico
plt.show()




ax.set_title('Relación entre la cuenta total y la propina', fontsize=14, color='blue', fontweight='bold')




import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
datos = sns.load_dataset('tips')

# Crear una cuadrícula de gráficos
g = sns.FacetGrid(datos, col='time')
g.map(sns.histplot, 'total_bill')

# Agregar un título a cada gráfico
g.set_titles('Hora del día: {col_name}')

# Agregar un título general a la figura
g.figure.suptitle('Distribución de la cuenta total por hora del día', fontsize=16)

# Ajustar los espacios
g.figure.tight_layout()

# Mostrar los gráficos
plt.show()




import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
datos = sns.load_dataset('penguins')

# Crear un gráfico de dispersión
ax = sns.scatterplot(data=datos, x='bill_length_mm', y='bill_depth_mm')

# Añadir etiquetas a los ejes
ax.set_xlabel('Longitud del pico (mm)')
ax.set_ylabel('Profundidad del pico (mm)')

# Mostrar el gráfico
plt.show()





# Añadir una anotación en el gráfico
ax.text(45, 17, 'Pico largo y profundo', fontsize=12, color='red')

# Mostrar el gráfico
plt.show()




# Seleccionar un punto de interés
x_anot = datos['bill_length_mm'].mean()
y_anot = datos['bill_depth_mm'].mean()

# Añadir una anotación con una flecha
ax.annotate('Media de valores', xy=(x_anot, y_anot), xytext=(55, 15),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=12, ha='center')

# Mostrar el gráfico
plt.show()



# Crear un gráfico con FacetGrid
g = sns.relplot(data=datos, x='bill_length_mm', y='bill_depth_mm', col='species')

# Añadir etiquetas de los ejes
g.set_axis_labels('Longitud del pico (mm)', 'Profundidad del pico (mm)')

# Añadir texto en la figura
g.figure.text(0.5, 1.0, 'Datos de pingüinos de Palmer Archipelago', ha='center', fontsize=12)

# Mostrar el gráfico
plt.show()





import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
datos = sns.load_dataset('penguins')

# Crear un gráfico de dispersión
ax = sns.scatterplot(data=datos, x='bill_length_mm', y='bill_depth_mm')

# Personalizar etiquetas de los ejes con estilos
ax.set_xlabel('Longitud del pico (mm)', fontsize=14, fontweight='bold', color='darkgreen')
ax.set_ylabel('Profundidad del pico (mm)', fontsize=14, fontweight='bold', color='darkblue')

# Mostrar el gráfico
plt.show()





# Añadir una anotación con un recuadro
ax.text(50, 20, 'Zona de interés',
        bbox=dict(facecolor='yellow', alpha=0.5),
        fontsize=12)

# Mostrar el gráfico
plt.show()





# Rotar etiquetas del eje X
plt.setp(ax.get_xticklabels(), rotation=45)

# Mostrar el gráfico
plt.show()





import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
datos = sns.load_dataset('iris')

# Crear un gráfico de dispersión con 'hue' basado en la especie
ax = sns.scatterplot(data=datos, x='sepal_length', y='sepal_width', hue='species')

# Mostrar el gráfico
plt.show()





# Ubicar la leyenda en la esquina superior izquierda
ax.legend(loc='upper left')

# Mostrar el gráfico
plt.show()




# Cambiar el título de la leyenda
ax.legend(title='Tipo de Iris')

# Mostrar el gráfico
plt.show()





# Obtener los handles y labels actuales
handles, labels = ax.get_legend_handles_labels()

# Definir nuevas etiquetas
nuevas_etiquetas = ['Iris Setosa', 'Iris Versicolor', 'Iris Virginica']

# Actualizar la leyenda con las nuevas etiquetas
ax.legend(handles=handles, labels=nuevas_etiquetas, title='Tipo de Iris')

# Mostrar el gráfico
plt.show()





# Eliminar la leyenda del gráfico
ax.get_legend().remove()

# Mostrar el gráfico
plt.show()





# Gráfico con variables 'hue' y 'style'
ax = sns.scatterplot(data=datos, x='sepal_length', y='sepal_width', hue='species', style='species')

# Mostrar el gráfico
plt.show()





import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
datos = sns.load_dataset('iris')

# Crear un gráfico de dispersión con 'hue' basado en la especie
ax = sns.scatterplot(data=datos, x='sepal_length', y='sepal_width', hue='species')

# Personalizar detalles de la leyenda
ax.legend(title='Tipo de Iris',
          title_fontsize=12,
          fontsize=10,
          facecolor='lightgrey',
          edgecolor='black')

# Mostrar el gráfico
plt.show()






# Gráfico relacional con FacetGrid
g = sns.relplot(data=datos, x='sepal_length', y='sepal_width', hue='species', col='species')

# Ajustar el título de la leyenda
g.legend.set_title('Tipo de Iris')

# Mostrar el gráfico
plt.show()



# Eliminar la leyenda en FacetGrid
g._legend.remove()

# Mostrar el gráfico
plt.show()






# Renombrar categorías en el DataFrame
datos['species'] = datos['species'].map({'setosa': 'Setosa', 'versicolor': 'Versicolor', 'virginica': 'Virgínica'})

# Crear el gráfico con las etiquetas actualizadas
ax = sns.scatterplot(data=datos, x='sepal_length', y='sepal_width', hue='species')

# Mostrar el gráfico
plt.show()






import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un conjunto de datos de ejemplo
datos = sns.load_dataset('iris')

# Crear subgráficos
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Primer gráfico sin leyenda
sns.scatterplot(data=datos, x='sepal_length', y='sepal_width', hue='species', ax=axes[0], legend=False)

# Segundo gráfico sin leyenda
sns.scatterplot(data=datos, x='petal_length', y='petal_width', hue='species', ax=axes[1], legend=False)

# Añadir una leyenda común
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', ncol=3, title='Tipo de Iris')

# Ajustar espaciado
plt.tight_layout()

# Mostrar los gráficos
plt.show()
